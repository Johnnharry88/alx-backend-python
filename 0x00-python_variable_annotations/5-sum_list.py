#!/usr/bin/env python3
"""Annotated funstion that takes input_list
of float and returns their sum"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum as a float"""
    return float(sum(input_list))
