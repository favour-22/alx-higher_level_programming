#!/usr/bin/python3
"""
Module containing a function that prints a square 

"""


def print_square(size):
    """function that prin ts a square using # 
    
    Agrs:
         size (int): The size of one side of the square.
    """

    if type(size) is not  int :
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be an integer")

    print(('#' * size + '\n') * size, end='')
