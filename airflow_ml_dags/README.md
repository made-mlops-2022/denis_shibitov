# Homework 3: Airflow

Для запуска и корректной работы необходимо указать несколько параметров:
~~~
# для корректной работы с переменными, созданными из UI
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")

# директория на хост машине для хранения данных
export LOCAL_DATA_DIR=<data folder on host machine>

# логин и пароль к почте для отправке уведомлений
export SMTP_USER=<email>
export SMTP_PASSWORD=<email password>
~~~

Если все переменные установлены, можно выполнить сборку и запуск:
~~~
docker compose up --build
~~~

