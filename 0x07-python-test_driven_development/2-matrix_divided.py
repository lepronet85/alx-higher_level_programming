#!/usr/bin/python3

"""Defines a matrix division function."""


def divide_matrix(matrix, divisor):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The divisor.
    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("Input matrix must be a list of lists of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, int) and not isinstance(divisor, float):
        raise TypeError("Divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    return [
        [round(element / divisor, 2) for element in row]
        for row in matrix
    ]
