import os
from airflow import DAG
from airflow.models import Variable
from airflow.sensors.python import PythonSensor
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount


DEFAULT_MODEL_PATH = "/data/models/2022-12-02/model.pkl"


def _wait_for_files(*args):
    for file_path in args:
        if not os.path.exists(file_path):
            return False
    return True


with DAG(
    "predict",
    catchup=False,
    start_date=days_ago(1),
    schedule_interval="0 7 * * *"
) as dag:
    wait_for_data = PythonSensor(
        task_id="wait_for_data",
        python_callable=_wait_for_files,
        op_args=['/opt/airflow/data/raw/{{ ds }}/data.csv'],
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke"
    )
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="--input_dir /data/raw/{{ ds }} --output_dir /data/processed/test/{{ ds }} --data_type test",
        network_mode="bridge",
        auto_remove=True,
        task_id="test_preprocess",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )
    predict = DockerOperator(
        image="airflow-predict",
        command="--input_dir /data/processed/test/{{ ds }} --output_dir /data/predictions/{{ ds }} "
                f"--model_path {Variable.get('model_path', default_var=DEFAULT_MODEL_PATH)}",
        network_mode="bridge",
        auto_remove=True,
        task_id="predict",
        do_xcom_push=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )

    wait_for_data >> preprocess >> predict
