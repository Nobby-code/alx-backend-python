#!/usr/bin/env python3
""" asynchronous coroutine """


async def wait_random(max_delay: int = 10) -> float:
    """ function to delay for a period of 0-max_delay
    then return the period
    """
    delay_period: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_period)
    return delay_period
