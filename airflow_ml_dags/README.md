# airflow-examples
код для пары Data Pipelines

чтобы развернуть airflow, предварительно собрав контейнеры
~~~
# для корректной работы с переменными, созданными из UI
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
export LOCAL_DATA_DIR=.../airflow_ml_dags/data
docker compose up --build
~~~
Ссылка на документацию по docker compose up

https://docs.docker.com/compose/reference/up/
