import sys
import json
import logging

import requests
import pandas as pd


def _get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s]: %(message)s"
    )
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger


def _make_requests():
    logger = _get_logger('requests_maker')

    persons_data = pd.read_csv('persons_data.csv').drop('condition', axis=1)
    data_requests = persons_data.to_dict(orient='records')

    for request in data_requests:
        logger.debug('Request:%s', request)
        response = requests.post(
            'http://127.0.0.1:4242/predict',
            json.dumps(request)
        )
        logger.debug('Response code:%s. Response:%s', response.status_code, response.json())


if __name__ == '__main__':
    _make_requests()
