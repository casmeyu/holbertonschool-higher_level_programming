#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    if tuple_a[0]:
        tuple_c = (tuple_a[0], 0)

    if tuple_b[0]:
        tuple_c = ((tuple_c[0] + tuple_b[0]), 0)

    if tuple_a[1]:
        tuple_c = (tuple_c[0], tuple_a[1])

    if tuple_b[1]:
        tuplce_c = (tuple_c[0], (tuple_c[1] + tuple_b[1]))

    return (tuple_c)
