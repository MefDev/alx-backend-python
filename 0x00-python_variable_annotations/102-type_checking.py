#!/usr/bin/env python3
"""types of the elements of the input are not known"""

from typing import List


def zoom_array(lst: List, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in * int(factor)
