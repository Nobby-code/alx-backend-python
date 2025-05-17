#!/usr/bin/env python3
""" List conprehension with async """

from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ returns a list of 10 random numbers """

    return [i async for i in async_generator()]
