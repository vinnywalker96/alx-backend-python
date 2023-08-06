#!/usr/bin/env python3
"""
to_kv_takes string and int/float and returns tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2)
