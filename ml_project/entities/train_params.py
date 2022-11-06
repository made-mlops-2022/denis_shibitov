"""Model parameters module"""
from dataclasses import dataclass, field


@dataclass
class TrainingParams:
    """Model parameters dataclass"""
    model_type: str = field(default="RandomForestClassifier")
    random_state: int = field(default=255)
