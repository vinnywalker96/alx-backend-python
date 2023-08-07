#!/usr/bin/env python3
""" import """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    return lambda y: multiplier * y
