#!/usr/bin/python3
"""A module that append a string at the end of a text file"""

def append_write(filename="", text=""):
    """append a string at the end of a text file"""

    with open(filename, mode="a", encoding = "utf-8") as f:
        return f.write(text)
