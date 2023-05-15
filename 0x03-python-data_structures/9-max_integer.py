#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    bg = 0
    if len(my_list) == 0:
        return (None)
    if ln != 0:
        for i in my_list:
            if i > bg:
                bg = i
        return (bg)
    else:
        return (None)
