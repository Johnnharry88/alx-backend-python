#!/usr/bin/env python3
"""Annotated function that takes a list of mixed 
numbers [integer and float] and returns sum as a float
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns sum of the list as float"""
    return float(sum(mxd_lst))
