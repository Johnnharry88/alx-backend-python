#!/usr/bin/env python3
"""Coroutine that will collect 10 random numbers using async
comprehensing voer async_generator and returns the 10 random numbers"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers"""
    res = [x async for x in async_generator()]
    return res
