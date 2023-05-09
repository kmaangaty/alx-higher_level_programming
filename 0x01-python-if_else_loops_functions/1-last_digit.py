#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
type_one = "and is less than 6 and not 0"
type_tow = "and is greater than 5"
if number != 0 and last_digit != 0:
    if number < 0:
        print(f"Last digit of {number} is -{last_digit} {type_one}")
    else:
        if last_digit < 6:
            print(f"Last digit of {number} is {last_digit} {type_one}")
        else:
            print(f"Last digit of {number} is {last_digit} {type_tow}")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
