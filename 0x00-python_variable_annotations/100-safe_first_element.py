#!/usr/bin/env python3
"""Augmentint code with the correct duct typed annotations
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Dock Tped annotations"""
    if lst:
        return lst[0]
    else:
        return None
