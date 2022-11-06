"""Predict pipeline parameters module"""
from dataclasses import dataclass
import yaml
from marshmallow_dataclass import class_schema


@dataclass
class PredictPipelineParams:
    """Predict pipeline parameters dataclass"""
    data_path: str
    target_col: str
    model_path: str
    predict_result_path: str


PredictPipelineParamsSchema = class_schema(PredictPipelineParams)


def read_predict_pipeline_params(path: str) -> PredictPipelineParams:
    """Read predict pipeline parameters from file"""
    with open(path, "r") as input_stream:
        schema = PredictPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
