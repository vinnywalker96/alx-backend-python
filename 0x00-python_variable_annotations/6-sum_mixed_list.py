#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union

Type = List[Union[int, float]]


def sum_mixed_list(mxd_lst: Type) -> Type:
    """Return the sum of a list of floats and ints"""
    return sum(mxd_lst)
