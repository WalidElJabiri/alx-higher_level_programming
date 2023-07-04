#!/usr/bin/python3
"""

function that divides the nums of the matrix

"""

def matrix_divided(matrix, div):
    """ Function that divides the int/float nums of the matrix
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg)

    lenn = 0
    size_msg = "Each row of the matrix must have the same size"

    for e in matrix:
        if not e or not isinstance(e, list):
            raise TypeError(msg)

        if lenn != 0 and len(e) != lenn:
            raise TypeError(size_msg)

        for num in e:
            if not type(num) in (int, float):
                raise TypeError(msg)

        lenn = len(e)

    n = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (n)
