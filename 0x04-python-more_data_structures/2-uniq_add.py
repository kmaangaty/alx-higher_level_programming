#!/usr/bin/python3
def uniq_add(my_list=[]):
    rs = 0
    for x in set(my_list):
        rs += x
    return rs
