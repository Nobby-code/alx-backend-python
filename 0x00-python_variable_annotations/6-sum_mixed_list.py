#!/usr/bin/env python3
""" function that takes in a list of integers and floats """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return the sum of list items as a float """
    sum: float = 0
    for x in mxd_lst:
        sum += x
    return sum
