#!/usr/bin/env python3
def isnum(value):
    """Return value if it's a number, else 0."""
    return value if isinstance(value, (int, float)) else 0


def add_tuple(tuple_a=(), tuple_b=()):
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    return (isnum(a[0]) + isnum(b[0]), isnum(a[1]) + isnum(b[1]))
