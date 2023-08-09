#!/usr/bin/env python3
"""Basic async"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: _description_
    """
    start = time.perf_counter()
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    time_elapsed = time.perf_counter() - start

    return f'{time_elapsed}'


print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
