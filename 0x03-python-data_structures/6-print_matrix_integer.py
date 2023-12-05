#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            print()
        else:
            for j in range(len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]), end='\n')
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
