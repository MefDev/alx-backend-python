#!/usr/bin/env python3
"""sum float numbers in a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum float numbers in a list"""
    return sum(mxd_lst)
