#!/usr/bin/env python3
"""Find Length of Element"""
from typing import List, Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element Length

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence]]: _description_
    """
    return [(i, len(i)) for i in lst]
