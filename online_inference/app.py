import os
import pickle
import pandas as pd
from fastapi import FastAPI

from person_parameters import PersonParameters


model = None
app = FastAPI()


@app.on_event('startup')
def load_model():
    path_to_model = os.getenv('MODEL_PATH')
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
