#!/usr/bin/env python3
"""Annotated function that takes string and float or int
and returns a tuple first telement being strng"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Return a tuple of strung and squae of number"""
    return (k, float(v * v))
