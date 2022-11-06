import unittest
import numpy as np
import pandas as pd

from ml_project.features import SquareTransformer
from ml_project.train_pipeline import run_train_pipeline


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


class RandomTrainDataPipelineTest(unittest.TestCase):
    def test_random_train_data_test(self):
        make_random_train_data(300)

        run_train_pipeline("tests/random_train_config.yaml")
        self.assertEqual(0, 0)



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
