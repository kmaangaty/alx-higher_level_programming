#!/usr/bin/python3
def pow(a, b):
    to_re = a
    for i in range(b-1):
        to_re = a * to_re
    return to_re
