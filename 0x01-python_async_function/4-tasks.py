#!/usr/bin/env python3
"""Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: list of delays
    """
    tasks = [task_wait_random(n) for _ in range(max_delay)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
