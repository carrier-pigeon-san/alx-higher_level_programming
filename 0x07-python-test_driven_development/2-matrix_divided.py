#!/usr/bin/python3
"""matrix_divided() function module"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divides all elements of a matrix
    @matrix: given matrix
    @div: value, matrix elements are to be divided by
    """

    if type(matrix) is list:
        for item in range(len(matrix)):
            if type(matrix[item]) is list:
                if item == 0:
                    row_size = len(matrix[item])
                if len(matrix[item]) != row_size:
                    raise TypeError(
                            "Each row of the matrix must have the "
                            "same size"
                            )
                for element in matrix[item]:
                    if type(element) is not int and type(element) is not float:
                        raise TypeError(
                                "matrix must be a matrix "
                                "(list of lists) of integers/floats"
                                )
            else:
                raise TypeError(
                        "matrix must be a matrix (list of lists) "
                        "of integers/floats"
                        )
    else:
        raise TypeError(
                "matrix must be a matrix (list of lists) "
                "of integers/floats"
                )

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    matrix2 = [[round(j/div, 2) for j in i] for i in matrix]

    return matrix2
