#!/usr/bin/env python3
""" type-annotated function for multiplication """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function to return a function"""
    return (lambda x: multiplier * x)
