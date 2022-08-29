#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b, c, d = 0, 0, 0, 0

    if len(tuple_a) == 1:
        a = tuple_a[0]
    elif len(tuple_a) >= 2:
        a, b = tuple_a[:2]
    if len(tuple_b) == 1:
        c = tuple_b[0]
    elif len(tuple_b) >= 2:
        c, d = tuple_b[:2]

    return (a + c, b + d)
