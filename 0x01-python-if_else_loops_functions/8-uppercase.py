#!/usr/bin/python3
def uppercase(str):
    str_main = str
    for i in range(len(str)):
        if 97 <= ord(str_main[i]) <= 122:
            str_main = str_main[:i] + chr(ord(str_main[i]) - 32) + str_main[i + 1:]
    print("{}".format(str_main))
