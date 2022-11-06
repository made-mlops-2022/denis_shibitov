"""Data operation functions module"""
import json
import pickle
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from ml_project.entities import SplittingParams


BINARY = "binary"
JSON = "json"


def read_data(path: str) -> pd.DataFrame:
    """Get dataset from path"""
    data = pd.read_csv(path)
    return data


def split_train_val_data(
    data: pd.DataFrame, params: SplittingParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Split dataset to two part"""

    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data


def save_object(obj: object, path: str, save_as=BINARY):
    """Save object to path"""
    if save_as == BINARY:
        with open(path, "wb") as file:
            pickle.dump(obj, file)
    elif save_as == JSON:
        with open(path, "w", encoding='utf-8') as file:
            json.dump(obj, file)
    else:
        raise NotImplementedError()


def load_object(path: str, load_as=BINARY) -> object:
    """Load stored object from path"""
    if load_as == BINARY:
        with open(path, "rb") as file:
            return pickle.load(file)
    elif load_as == JSON:
        with open(path, "r", encoding='utf-8') as file:
            return json.load(file)
    else:
        raise NotImplementedError()
