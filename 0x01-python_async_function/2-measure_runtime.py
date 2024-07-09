#!/usr/bin/env python3
"""Function that takes integer and max_delay
and measure the total execution time for wait_n
(n, max_delay) and returns a float
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the sum total of execution time"""
    time_start = time.time()
    asyncio.run(waiter(n, max_delay))
    time_end = time.time()
    total_time = time_end = time_start
    return (total_time/n)
