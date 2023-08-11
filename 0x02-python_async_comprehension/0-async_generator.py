#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, float]:
    """_summary_

    Returns:
        float: _description_

    Yields:
        Iterator[float]: _description_
    """
    for i in range(10):
        await asyncio.sleep(1)
        delay = random.uniform(0, i)
        yield delay
