#!/usr/bin/env python3
""" type-annotated function which takes a list of arguments
    returns the sum of the list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of the list items (float) """
    sum: float = 0
    for x in input_list:
        sum += x
    return sum
