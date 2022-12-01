"""Model operation functions module"""
from typing import Dict, Union
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

from ml_project.entities.train_params import TrainingParams


SklearnClassificationModel = Union[LogisticRegression, RandomForestClassifier]


def train_model(features: pd.DataFrame,
                target: pd.Series,
                train_params: TrainingParams
                ) -> SklearnClassificationModel:
    """Process model training"""

    if train_params.model_type == 'LogisticRegression':
        model = LogisticRegression()
    elif train_params.model_type == 'RandomForestClassifier':
        model = RandomForestClassifier()
    else:
        raise NotImplementedError(f'Unknown model type:{train_params.model_type}')

    model.fit(features, target)

    return model


def create_inference_pipeline(
    model: SklearnClassificationModel, transformer: ColumnTransformer
) -> Pipeline:
    """Get inference pipeline for transformer and model"""
    pipeline_parts = []
    if transformer:
        pipeline_parts.append(("feature_part", transformer))
    pipeline_parts.append(("model_part", model))

    return Pipeline(pipeline_parts)


def predict_model(model: Pipeline, features: pd.DataFrame) -> np.ndarray:
    """Get model predictions"""
    return model.predict(features)


def evaluate_model(predict: np.ndarray, target: pd.Series) -> Dict[str, float]:
    """Calculate metrics for model predictions"""
    return {
        'accuracy': accuracy_score(target, predict),
        'f1': f1_score(target, predict, average='macro')
    }
