import os
import unittest
import numpy as np
import pandas as pd

from ml_project.features import SquareTransformer
from ml_project.train_pipeline import train_pipeline
from ml_project.predict_pipeline import predict_pipeline

from ml_project.entities import (
    read_training_pipeline_params,
    read_predict_pipeline_params
)

from ml_project.data import (
    save_object,
    load_object
)


class SquareTransformerTest(unittest.TestCase):
    def test_transformation_normal(self):
        data = pd.DataFrame([
            {'variable_1': -1, 'variable_2': 2},
            {'variable_1': 5, 'variable_2': -6},
        ])

        transformed_data = pd.DataFrame([
            {'variable_1': 1, 'variable_2': 4},
            {'variable_1': 25, 'variable_2': 36},
        ])

        transformer = SquareTransformer()
        result = transformer.transform(data)

        self.assertListEqual(list(transformed_data.columns), list(result.columns))
        self.assertEqual(transformed_data.values[0][0], result.values[0][0])
        self.assertEqual(transformed_data.values[0][1], result.values[0][1])
        self.assertEqual(transformed_data.values[1][0], result.values[1][0])
        self.assertEqual(transformed_data.values[1][1], result.values[1][1])

    def test_transformation_empty(self):
        data = pd.DataFrame()

        transformer = SquareTransformer()
        result = transformer.transform(data)
        self.assertEqual(list(data), list(result.values))


class DifferentModulesTest(unittest.TestCase):
    def test_save_load_object(self):
        obj = {"a": "100", "b": 300}
        obj_path = "tests/obj_for_test"

        save_object(obj, obj_path, save_as="json")
        loaded_obj = load_object(obj_path, load_as="json")
        self.assertEqual(obj, loaded_obj)

        save_object(obj, obj_path, save_as="binary")
        loaded_obj = load_object(obj_path, load_as="binary")
        self.assertEqual(obj, loaded_obj)


class TrainPredictPipelineTest(unittest.TestCase):
    def test_train_pipeline(self):
        config_path = "configs/train_config.yaml"
        model_path, metrics = train_pipeline(config_path)

        config = read_training_pipeline_params(config_path)

        self.assertEqual(model_path, config.output_model_path)
        self.assertEqual(os.path.exists(config.output_model_path), True)
        self.assertEqual(os.path.exists(config.metric_path), True)

        above_limit = metrics["accuracy"] > 0.5
        self.assertEqual(above_limit, True)

    def test_train_predict_pipeline(self):
        train_config_path = "configs/train_config.yaml"
        predict_config_path = "configs/predict_config.yaml"
        train_pipeline(train_config_path)
        predict_pipeline(predict_config_path)

        predict_config = read_predict_pipeline_params(predict_config_path)
        self.assertEqual(os.path.exists(predict_config.predict_result_path), True)

        test_data = pd.read_csv(predict_config.data_path)
        predict = pd.read_csv(predict_config.predict_result_path)
        self.assertEqual(len(test_data), len(predict))


class RandomTrainDataPipelineTest(unittest.TestCase):
    def test_random_train_data_test(self):
        make_random_train_data(300)

        model_path, metrics = train_pipeline("tests/random_train_config.yaml")
        above_limit = metrics["accuracy"] > 0.2
        self.assertEqual(above_limit, True)


def make_random_train_data(rows_count=500):
    data = {
        "age": pd.Series(np.random.randint(18, 91, size=rows_count)),
        "sex": pd.Series(np.random.randint(0, 2, size=rows_count)),
        "cp": pd.Series(np.random.randint(0, 4, size=rows_count)),
        "trestbps": pd.Series(np.random.randint(94, 201, size=rows_count)),
        "chol": pd.Series(np.random.randint(126, 565, size=rows_count)),
        "fbs": pd.Series(np.random.randint(0, 2, size=rows_count)),
        "restecg": pd.Series(2 * np.random.randint(0, 2, size=rows_count)),
        "thalach": pd.Series(np.random.randint(71, 203, size=rows_count)),
        "exang": pd.Series(np.random.randint(0, 2, size=rows_count)),
        "oldpeak": pd.Series(6.2 * np.random.random(size=rows_count)),
        "slope": pd.Series(np.random.randint(0, 3, size=rows_count)),
        "ca": pd.Series(np.random.randint(0, 3, size=rows_count)),
        "thal": pd.Series(np.random.randint(0, 3, size=rows_count)),
        "condition": pd.Series(np.random.randint(0, 2, size=rows_count))
    }
    data = pd.DataFrame(data)
    data.to_csv("tests/random_train_data.csv", index=False)
