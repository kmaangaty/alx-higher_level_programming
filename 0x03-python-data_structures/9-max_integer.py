#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    bg = 0
    if ln != 0:
        for i in my_list:
            if i > bg:
                bg = i
        return (bg)
    else:
        return (None)
