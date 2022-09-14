#!/usr/bin/python3
""'Module containing the square class""'


class Square:
    """The Square class"""
    def __init__(self,size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size

        def area(self):
            return  self.__size * self.__size
