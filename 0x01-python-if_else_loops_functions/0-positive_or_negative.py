#!/usr/bin/python3
number = random.randint(-10, 10)
if number > 0:
	msg = "is positive"
elif number == 0:
	msg = "is zero"
else:
	msg = "is positive"
print("{:d} {:s}".format(number, msg))

