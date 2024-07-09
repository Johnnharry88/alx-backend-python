#!/usr/bin/env python3
"""A function that measures time after importing
async_comprehension from 1-async_comprehension
"""


import asyncio
import time
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measres total runtime"""
    s_time = time.time()
    await asyncio.gather(*(async_comp() for x in range(4)))
    e_time = time.time()
    time_interval = e_time = s_time
    return time_interval
