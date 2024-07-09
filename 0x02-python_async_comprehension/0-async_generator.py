#!/usr/bin/env python3
"""Function async_generator that takes no arguments
and returns a number between 0 and 10
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times and waits for 1 second each time a loop
    is completed"""
    for a in range(10):
        await asyncio.sleep(1)
        x = random.random() * 10
        yield x
