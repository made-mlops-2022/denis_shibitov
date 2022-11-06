"""Square transformer module"""
from typing import List
from dataclasses import dataclass


@dataclass
class SquareTransformerParams:
    """Square transformer dataclass"""
    columns_for_square: List[str]
