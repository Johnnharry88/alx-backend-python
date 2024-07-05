#!/usr/bin/env python3
"""Annotated function that takes a float multiplier and
returns a function that multiplies a float by multiplier
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a float by mulitiplier"""
    def multiplier_float(x: float) -> float:
        return multiplier * x

    return multiplier_float
