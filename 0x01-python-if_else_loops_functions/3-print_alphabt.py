#!/usr/bin/python3
stri = ''
for start in range(97, 123):
    if start != 101 and start != 113:
        to_print = "{:c}".format(start)
        stri = stri + to_print
print(stri, end='')
