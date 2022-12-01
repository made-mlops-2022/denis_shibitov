"""Split parameters module"""
from dataclasses import dataclass, field


@dataclass
class SplittingParams:
    """Split parameters dataclass"""
    val_size: float = field(default=0.2)
    random_state: int = field(default=42)
