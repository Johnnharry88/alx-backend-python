#!/usr/bin/env python3
"""Adding type annotation to the function looking at the 
given parameters"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                    typing.Union[T, None] = None) ->\
                    typing.Union[typing.Any, T]:
    """Annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
