#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mlr = len(my_list) - 1
    if idx > mlr:
        return my_list
    if idx < 0:
        return my_list
    nl = [i for i in my_list]
    nl[idx] = element
    return nl
