#!/usr/bin/env python3
"""Asyn function that takes in an int arg wit a
defaut value of 10 and waits for a random delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Delay function exe"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
