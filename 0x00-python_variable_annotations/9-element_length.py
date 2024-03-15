#!/usr/bin/env python3
"""element_length"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length"""
    return [(i, len(i)) for i in lst]
