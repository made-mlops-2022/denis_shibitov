MADE MLOps
==============================
###### homework 2
Inference модели с помощью REST-сервиса на FastAPI

### Денис Шибитов
<br>

#### Собрать docker образ локально: 
~~~
docker build -t ymet/made_oi:v1 .
~~~
#### Скачать готовый docker образ:
~~~
docker pull ymet/made_oi:v1 
~~~
#### Запустить docker образ:
~~~
docker run -d -p 4242:4242 --name made_oi ymet/made_oi:v1
~~~
#### Запустить скрипт с запросами (при запущенном сервисе/докер образе с ним):
~~~
python make_requests.py
~~~
#### Запуск тестов:
Используя локальную модель:
~~~
MODEL_PATH=model.pkl python -m unittest tests.py
~~~
Или доступную по url:
~~~
MODEL_PATH=https://disk.yandex.ru/d/CtY5RxXyYn6hfQ python -m unittest tests.py
~~~

### По поводу размера docker образа
Не долго думаю, хотел изначально воспользоваться в роли базового образа
чем то очевидным вроде "FROM ubuntu:16.04". Но для начала,
решил проверить что используется в примерах которые предоставили:
https://github.com/made-ml-in-prod-2021/inference_examples/blob/main/online_inference/Dockerfile

Название показалось намного более многообещающим чем просто ubuntu, так что сразу
попробовал FROM python:3.7-slim-stretch (версию python изменил на свою).
В итоге получил образ с COMPRESSED SIZE 151.64 MB

Результат кажется хорошим. Подумал, можно ли лучше?
Погуглив, ознакомился с несколькими заметками по этой теме:
https://pythonspeed.com/articles/base-image-python-docker-images/
https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
https://simonwillison.net/2018/Nov/19/smaller-python-docker-images/

Учитывая информацию в них, начал думать что python:3.7-alpine - то что мне нужно.
Но не срослось. Достаточно много времени боролся, но так и не получилось получить
рабочий образ - не удается установить все необходимые зависимости (requirements.txt).

В общем, остановился на python:3.7-slim-stretch. На сколько я могу судить, ~151 MB весьма
хороший результат.

