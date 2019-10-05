#!/usr/bin/python3
"""
function that divides a matrix in an integer
Args: matrix and integer
Return: new matrix divided
"""


def matrix_divided(matrix, div):
    """
    function that divides a matrix in an integer
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    for x in matrix:
        if type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")

    new_matrix = [x[:] for x in matrix]

    length = len(matrix[0])

    for i in range(len(matrix)):
        if len(new_matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(new_matrix[i][j]) is not int and type(new_matrix[i][j]) +
            is not float or type(new_matrix[i][j]) is None:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
            new_matrix[i][j] = round((matrix[i][j] / div), 2)

    return new_matrix
