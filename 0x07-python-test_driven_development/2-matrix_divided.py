#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix where all elements are divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
        or if div is not a number.
        TypeError: If each row of the matrix doesn't have the same size.
        ZeroDivisionError: If div is equal to 0.
    """

    is_matrix_list = isinstance(matrix, list)
    is_all_lists = all(isinstance(row, list) for row in matrix)
    if not (is_matrix_list and is_all_lists):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    is_same_size = all(len(row) == len(matrix[0]) for row in matrix)
    if not is_same_size:
        raise TypeError("Each row of the matrix must have the same size")

    is_div_number = isinstance(div, (int, float))
    if not is_div_number:
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
