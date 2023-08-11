#!/usr/bin/env python3
"""Async Compression"""
import asyncio
from typing import AsyncGenerator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """_summary_

    Returns:
        AsyncGenerator[float, None]: list of delays
    """
    return [item async for item in async_generator()]
