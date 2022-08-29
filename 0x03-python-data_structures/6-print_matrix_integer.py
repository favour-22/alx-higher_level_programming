#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("".format())
    for row in matrix:
        length = len(row)
        for i in range(length):
            if i < length - 1:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]))
