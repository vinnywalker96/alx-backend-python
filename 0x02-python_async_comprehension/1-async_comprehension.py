#!/usr/bin/env python3
"""Async Compression"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: list of delays
    """
    return [item async for item in async_generator()]
