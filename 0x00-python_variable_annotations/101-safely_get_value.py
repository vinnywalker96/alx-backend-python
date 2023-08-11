#!/usr/bin/env python3
"""Type Annotation"""
from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')
D = Union[T, None]
R = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """_summary_

    Args:
        dct (Mapping): _description_
        key (Any): _description_
        default (D, optional): _description_. Defaults to None.

    Returns:
        R: _description_
    """
    if key in dct:
        return dct[key]
    else:
        return default
