#!/usr/bin/python3
"""
A module to read a text file

"""

def read_file(filename=""):
    """Reads a text file and prints it to standard output"""
    with open("filename", encoding="utf-8") as f:
        for text in f:
            print(text, end="")
