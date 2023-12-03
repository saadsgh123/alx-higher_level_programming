#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if len(matrix) < 0 or matrix is None:
        print("")
    else:
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix)):
                print("{}".format(matrix[x][y]), end=" ")
            print("".format(""))
