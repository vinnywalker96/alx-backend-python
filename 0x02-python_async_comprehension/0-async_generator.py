#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> float:
    for _ in range(10):
        await asyncio.sleep(1)
        delay = random.uniform(0, 10)
        yield delay
