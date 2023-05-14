#!/usr/bin/python3
def element_at(my_list, idx):
    mlr = len(my_list) - 1
    if idx > mlr:
        return None
    if idx < 0:
        return None
    return(my_list[idx])
