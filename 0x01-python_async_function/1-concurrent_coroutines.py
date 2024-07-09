#!/usr/bin/env python3
"""Function htat returns the list of all delays in float
vlaues in an ascending order without sort due to concureency
"""

from typing import List
import asyncio
wait_room = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """checks the wait_random n times"""
    works = []
    delay = []

    for x in range(n):
        task = wait_room(max_delay)
        works.append(task)

    for task in asyncio.as_completed((works)):
        d = await task
        delay.append(d)

    return delay
