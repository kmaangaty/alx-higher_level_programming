#!/usr/bin/python3
start_i = 0
max_i = 100
for i in range(start_i, max_i):
    if i == max_i - 1:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
