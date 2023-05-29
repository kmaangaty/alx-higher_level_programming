#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        clc = a / b
    except (TypeError, ZeroDivisionError):
        clc = None
    finally:
        print("Inside result: {}".format(clc))
    return (clc)
