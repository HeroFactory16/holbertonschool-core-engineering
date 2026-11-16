#!/usr/bin/env python3
def check_tuple(t=()):
    if not t[0]:
        t[0] = 0
    if not t[1]:
        t[1] = 0
    return t


def add_tuple(tuple_a=(), tuple_b=()):
    result = (0, 0)
    result[0] = check_tuple(tuple_a[0]) + check_tuple(tuple_b[0])
    result[1] = check_tuple(tuple_a[1]) + check_tuple(tuple_b[1])

    return result
