"""Square transformer module"""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class SquareTransformer(BaseEstimator, TransformerMixin):
    """Square transformer class"""

    def fit(self, data: pd.DataFrame) -> pd.DataFrame:
        # pylint: disable = unused-argument
        """Fit square transformer for numerical features"""
        return self

    def transform(self, data: pd.DataFrame):
        """Transform numerical features"""
        # pylint: disable = no-self-use
        for column in data.columns:
            data[column] = data[column].apply(lambda x: x ** 2)
        return data

    def fit_transform(self, X, y=None, **fit_params):
        """Fit and transform numerical features"""
        return self.transform(X)
