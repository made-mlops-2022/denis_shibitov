from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount


with DAG(
        "generate_data",
        catchup=False,
        start_date=days_ago(1),
        schedule_interval="0 5 * * *"
) as dag:
    generate_data = DockerOperator(
        image="airflow-generator",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        auto_remove=True,
        task_id="docker-data-generator",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source=Variable.get("LOCAL_DATA_DIR"),
                target="/data",
                type="bind",
            )
        ]
    )
