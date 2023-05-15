#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mtx in range(len(matrix)):
        for stx in range(len(matrix[mtx])):
            print("{:d}".format(matrix[mtx][stx]), end="")
            if stx != (len(matrix[mtx]) - 1):
                print(" ", end="")
        print("")
