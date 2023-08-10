#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
import time
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    list_delay: list[float] = []
    start = time.perf_counter()
    i = random.uniform(0, n)
    await asyncio.sleep(i)
    time_elapsed = time.perf_counter() - start
    list_delay.append(time_elapsed)
    return list_delay
