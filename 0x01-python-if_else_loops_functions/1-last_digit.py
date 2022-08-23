#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number <= 0:
     ld = ld * -1
if ld > 5:
   msg = "greater than 5"
elif ld == 0:
    msg = "0"
else:
    msg = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {:s}".format(number, ld, msg))
