#!/usr/bin/python3
def element_at(my_list, idx):
    mlr = len(my_list) - 1
    if idx > mlr:
        return
    if idx < 0:
        return
    return "Element at index {:d} is {}".format(idx, mylist[idx])
