"""Model feature parameters module"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FeatureParams:
    """Model feature parameters dataclass"""
    categorical_features: List[str]
    numerical_features: List[str]
    # features_to_drop: List[str]
    target_col: Optional[str]
    # use_log_trick: bool = field(default=True)
