""" Predicting pipline for model """
# pylint: disable=E0401, E0611, E1120
import sys
import logging
import click
import pandas as pd

from entities import read_predict_pipeline_params

from data import (
    read_data,
    load_object
)

from models.model_fit_predict import (
    predict_model
)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def predict_pipeline(config_path: str):
    """ predict pipeline """
    predict_pipeline_params = read_predict_pipeline_params(config_path)
    logger.info(
        'start predict pipeline with params %s',
        predict_pipeline_params
    )

    data = read_data(predict_pipeline_params.data_path)

    if predict_pipeline_params.target_col:
        data = data.drop(predict_pipeline_params.target_col, 1)

    logger.info('predicting..')
    inference_pipeline = load_object(predict_pipeline_params.model_path)
    predicts = predict_model(
        inference_pipeline,
        data
    )

    result = pd.Series(
        predicts,
        index=data.index,
        name=predict_pipeline_params.target_col
    )
    result.to_csv(predict_pipeline_params.predict_result_path, index=False)


@click.command(name='predict_pipeline')
@click.argument('config_path')
def predict_pipeline_command(config_path: str):
    """Pipeline entry point"""
    predict_pipeline(config_path)


if __name__ == '__main__':
    predict_pipeline_command()