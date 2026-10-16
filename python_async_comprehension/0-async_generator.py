#!/usr/bin/env python3
"""
An asynchronous generator coroutine that yields 10 random numbers
between 0 and 10, waiting 1 second asynchronously between each yield.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, waits 1 second,
    and yields a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
