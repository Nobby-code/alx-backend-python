#!/usr/bin/env python3
""" Takes str and int or float, returns tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns tuple """
    new_tup: Tuple[str, Union[int, float]] = (k, v**2)
    return new_tup
