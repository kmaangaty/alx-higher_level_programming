#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = my_list[:]
    for x in range(len(nl)):
        if nl[x] == search:
            nl[x] = replace
    return nl
