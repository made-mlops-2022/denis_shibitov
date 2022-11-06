"""Training pipeline parameters module"""
from typing import Optional, List
from dataclasses import dataclass

import yaml
from marshmallow_dataclass import class_schema

from .split_params import SplittingParams
from .feature_params import FeatureParams
from .train_params import TrainingParams
from .square_transformer_params import SquareTransformerParams


@dataclass
class TrainingPipelineParams:
    """Training pipeline parameters dataclass"""
    # pylint: disable = too-many-instance-attributes
    input_data_path: str
    output_model_path: str
    metric_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams
    use_transformers: Optional[List[str]] = None
    square_transformer_params: Optional[SquareTransformerParams] = None
    # downloading_params: Optional[DownloadParams] = None
    use_mlflow: bool = False
    # mlflow_uri: str = "http://18.156.5.226/"
    # mlflow_experiment: str = "inference_demo"


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    """Get training pipeline parameters from file"""
    with open(path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
