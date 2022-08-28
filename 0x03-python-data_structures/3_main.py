#!/usr/bin/python
def print_reversed_list_integer(my_list=[1,2,3,4,5,6]): 
    if isinstance(my_list, list):
        for i in reversed(my_list):
            print("{}".format(i))
print_reversed_list_integer()
