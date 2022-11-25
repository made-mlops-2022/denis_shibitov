import os
import pickle
import requests
from urllib.parse import urlencode
import pandas as pd
from fastapi import FastAPI

from person_parameters import PersonParameters

YA_DISK_API = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
HTTPS_PREF = 'https'
MODEL_PATH = 'model.pkl'


model = None
app = FastAPI()


def _load_model_from_ya_disk(url):
    response = requests.get(YA_DISK_API + urlencode(dict(public_key=url)))
    download_url = response.json()['href']

    response = requests.get(download_url)
    with open(MODEL_PATH, "wb") as model_file:
        model_file.write(response.content)


@app.on_event('startup')
def load_model():
    path_to_model = os.getenv('MODEL_PATH')

    if HTTPS_PREF in path_to_model.lower():
        _load_model_from_ya_disk(path_to_model)
        path_to_model = MODEL_PATH

    with open(path_to_model, 'rb') as f:
        global model
        model = pickle.load(f)


@app.get('/')
def root():
    return 'It is entry point of heart problems predictor'


@app.get('/health')
def health() -> bool:
    return not (model is None)


@app.post('/predict')
def get_predict(data: PersonParameters):
    prediction = model.predict(pd.DataFrame([data.dict()]))
    return str({'condition': prediction[0]})
