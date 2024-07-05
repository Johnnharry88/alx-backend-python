#!/usr/bin/env python3
""" Anotating the given function parameters and
returning values withappropriate types"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuple"""
    return [(i, len(i)) for i in int]
