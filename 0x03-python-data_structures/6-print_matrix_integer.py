#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if len(matrix) == 0 or len(matrix[0]) == 0:
        print("")
    else:
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                print("{:d}".format(matrix[x][y]), end=" ")
            print("")
