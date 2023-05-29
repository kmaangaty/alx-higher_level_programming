#!/usr/bin/python3
def magic_calculation(a, b):
    clc = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            clc += a ** b / i
        except Exception:
            clc = b + a
            break
    return clc
