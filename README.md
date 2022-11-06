MADE MLOps
==============================
###### homework 1
### Денис Шибитов

Установка: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install .
~~~
Запуск обучения:
~~~
python ml_project/train_pipeline.py configs/train_config.yaml
~~~

Prediction:
~~~
python ml_project/predict_pipeline.py configs/predict_config.yaml
~~~


Test:
~~~
python -m unittest discover tests
~~~

~~~
├── source_data
├── configs
│             ├── predict_config.yaml
│             ├── train_config_log.yaml
│             ├── train_config_rf.yaml
│             └── train_config.yaml
├── EDA
│             ├── EDA_1.ipynb
│             ├── eda_report.html
│             └── eda_script.py
├── ml_project
│             ├── data
│             ├── entities
│             ├── features
│             ├── models
│             ├── predict_pipeline.py
│             └── train_pipeline.py
│             ├── __init__.py
├── requirements.txt
├── README.md
├── results
├── setup.py
└── tests
~~~