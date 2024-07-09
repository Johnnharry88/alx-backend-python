#!/usr/bin/env python3
"""Altering code wait_n into a callable
function"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Sapwns wait random witn the n input"""
    task = []
    waiter = []

    for x in range(n):
        t = task_wait_random(max_delay)
        task.append(t)

    for t in asyncio.as_completed((task)):
        delay = await t
        waiter.append(delay)

    return waiter
