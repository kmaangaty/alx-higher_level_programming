#!/usr/bin/python3
def no_c(my_string):
    nst = ""
    for i in my_string:
        if i != "c" and i != "C":
            nst = nst + i
    return nst
