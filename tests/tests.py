import unittest
import pandas as pd

from ml_project.features import SquareTransformer


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
