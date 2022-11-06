"""Building features functions module """
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from ml_project.entities import (
    FeatureParams,
    TrainingPipelineParams
)

from .square_transformer import SquareTransformer


def extract_target(data: pd.DataFrame, params: FeatureParams) -> pd.Series:
    """Get target column values"""
    return data[params.target_col]


def build_transformer(params: TrainingPipelineParams) -> ColumnTransformer:
    """Get data transformer object"""
    if not params.use_transformers:
        return None

    needed_transformers = [
        (
            "numerical_pipeline",
            build_numerical_pipeline(),
            params.feature_params.numerical_features,
        )
    ]
    if "ohe" in params.use_transformers:
        needed_transformers.append(
            (
                'categorical_pipeline',
                build_categorical_pipeline(),
                params.feature_params.categorical_features,
            )
        )
    if "square" in params.use_transformers:
        needed_transformers.append(
            (
                'square_pipeline',
                build_square_pipeline(),
                params.square_transformer_params.columns_for_square,
            )
        )

    return ColumnTransformer(needed_transformers)


def build_categorical_pipeline() -> Pipeline:
    """Get one hot encoding transformer for categorical features"""
    categorical_pipeline = Pipeline([
            ('OHE', OneHotEncoder()),
        ])

    return categorical_pipeline


def build_numerical_pipeline() -> Pipeline:
    """Get mean impute transformer for numeric features"""
    num_pipeline = Pipeline([
        ("impute", SimpleImputer(missing_values=np.nan, strategy="mean")),
    ])
    return num_pipeline


def build_square_pipeline() -> Pipeline:
    """Get square transformer for numeric features"""
    square_pipeline = Pipeline([
        ('square', SquareTransformer())
    ])

    return square_pipeline


def make_features(
        transformer: ColumnTransformer,
        data: pd.DataFrame
) -> pd.DataFrame:
    """Do data transformation with transformer"""
    if transformer:
        result = transformer.transform(data)
    else:
        result = data
    return result
