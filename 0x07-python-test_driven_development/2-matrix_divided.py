#!/usr/bin/python3
"""Divide elements in matrix.
Args:
    matrix (list): A list of lists of ints or floats.
    div (int/float): The divisor.
Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats.
    TypeError: ach row of the matrix must have the same size.
    TypeError: div must be a number.
    ZeroDivisionError: division by zero.
Returns:
    A new matrix representing the result of the division.
"""


def matrix_divided(matrix, div):
    """Divide elements in matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: ach row of the matrix must have the same size.
        TypeError: div must be a number.
        ZeroDivisionError: division by zero.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(saf, list) for saf in matrix) or
            not all((isinstance(snf, int) or isinstance(snf, float))
                    for snf in [rkm for saf in matrix for rkm in saf])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(saf) == len(matrix[0]) for saf in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), saf)) for saf in matrix]
