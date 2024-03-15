#!/usr/bin/env python3
"""make multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier function"""
    return lambda multi: multi * multiplier
