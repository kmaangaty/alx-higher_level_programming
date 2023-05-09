#!/usr/bin/python3
str_print = ""
for i in range(0, 100):
    if i < 10:
        str_print = str_print + "0{:d}".format(i)
    else:
        str_print = str_print + "{:d}".format(i)
    if i != 99:
        str_print = str_print + ", "
print(str_print)
