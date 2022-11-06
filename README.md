MADE MLOps
==============================
###### homework 1
Учебный проект, включающий обучение модели и получение предсказаний
сердечных заболеваний с её помощью.

### Денис Шибитов
<br>

#### Установка: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install .
~~~
#### Запуск обучения:
~~~
python ml_project/train_pipeline.py configs/train_config.yaml 
~~~
Так же дополнительно доступно ещё две различные
конфигурации для обучения:
~~~
train_config_rf.yaml
train_config_log.yaml
~~~

#### Предсказание:
~~~
python ml_project/predict_pipeline.py configs/predict_config.yaml
~~~

Результаты обучения, предсказания и полученные метрики качества
расположены в (можно изменить в файлах конфигурации):
~~~
results/models
results/predicts
results/metrics
~~~

#### Запуск тестов:
~~~
python -m unittest discover tests
~~~

#### Структура проекта:
~~~
├── source_data                             <- данные для обучения
├── configs                                 <- конфигурации для обучения и предсказания
│             ├── predict_config.yaml
│             ├── train_config_log.yaml
│             ├── train_config_rf.yaml
│             └── train_config.yaml
├── EDA                                     <- EDA: ноутбук + сгенерированный отдельно отчет
│             ├── EDA_1.ipynb
│             ├── eda_report.html
│             └── eda_script.py
├── ml_project
│             ├── data                      <- подмодуль для работы с данными
│             ├── entities                  <- дата классы для работы с конфигами
│             ├── features                  <- подмодуль для работы с предикторами
│             ├── models                    <- подмодуль для функций обучения/предсказаний
│             ├── predict_pipeline.py       <- получение предсказаний
│             └── train_pipeline.py         <- обучение модели на данных
│             ├── __init__.py
├── requirements.txt                        <- зависимости проекта
├── README.md                               <- описание проекта
├── results                                 <- каталог по умолчанию для полученных артефактов
├── setup.py
└── tests                                   <- тестирование кода
~~~