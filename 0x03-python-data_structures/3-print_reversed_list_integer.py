#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for i in reversed(my_list):
            print("{:d}".format(i))
