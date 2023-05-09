#!/usr/bin/python3
def remove_char_at(str, n):
    str_main = str
    str_main = str_main[:n] + '' + str_main[n + 1:]
    print("{}".format(str_main))
