import os
from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.sensors.python import PythonSensor
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount


def _wait_for_files(*args):
    for file_path in args:
        if not os.path.exists(file_path):
            return False
    return True


with DAG(
    "train",
    catchup=False,
    start_date=days_ago(8),
    schedule_interval="0 6 * * 1"
) as dag:
    wait_for_data = PythonSensor(
        task_id="wait_for_data",
        python_callable=_wait_for_files,
        op_args=['/opt/airflow/data/raw/{{ ds }}/data.csv',
                 '/opt/airflow/data/raw/{{ ds }}/target.csv'],
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke"
    )
    preprocessing = DockerOperator(
        image="airflow-preprocess",
        command="--input_dir /data/raw/{{ ds }} --output_dir /data/processed/train/{{ ds }} --data_type train",
        network_mode="bridge",
        auto_remove=True,
        task_id="preprocess",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )
    splitting = DockerOperator(
        image="airflow-split",
        command="--input_dir /data/processed/train/{{ ds }} --output_dir /data/splitted/{{ ds }}",
        network_mode="bridge",
        auto_remove=True,
        task_id="split",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )
    train = DockerOperator(
        image="airflow-train",
        command="--input_dir /data/splitted/{{ ds }} --models_dir /data/models/{{ ds }}",
        network_mode="bridge",
        auto_remove=True,
        task_id="train",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )
    validation = DockerOperator(
        image="airflow-validation",
        command="--input_dir /data/splitted/{{ ds }} --output_dir /data/metrics/{{ ds }} "
                "--models_dir /data/models/{{ ds }}",
        network_mode="bridge",
        auto_remove=True,
        task_id="validation",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )

    wait_for_data >> preprocessing >> splitting >> train >> validation
