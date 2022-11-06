MADE MLOps
==============================
Homework 1 project

Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install .
~~~
Usage:
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