#!/usr/bin/env python3
"""Measures time"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time

    Args:
        n (int): argument
        max_delay (int): argument

    Returns:
        float: total time divided by n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
