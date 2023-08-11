#!/usr/bin/env python3
"""Tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> any:
    """_summary_

    Args:
        max_delay (int): _description_

    Returns:
        _type_: _description_
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
