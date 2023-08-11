#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import AsyncGenerator, Any
import random


async def async_generator() -> AsyncGenerator[float, Any]:
    """_summary_

    Returns:
        float: _description_

    Yields:
        Iterator[float]: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        delay = random.uniform(0, 10)
        yield delay
