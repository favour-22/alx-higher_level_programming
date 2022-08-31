#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_sum = 0
    for i in range(1, len(argv)):
        arg_sum += int(argv[i])
    print("{:d}".format(arg_sum))
