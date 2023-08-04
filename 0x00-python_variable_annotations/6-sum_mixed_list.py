#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: list[Union[int, float]]):
    """Return the sum of a list of floats and ints"""
    return sum(mxd_lst)
