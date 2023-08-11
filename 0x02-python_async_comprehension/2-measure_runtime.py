#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
from typing import Coroutine, Any
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    start = time.perf_counter()
    tasks = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    return elapsed
