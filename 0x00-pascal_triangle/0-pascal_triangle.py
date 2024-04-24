#!/usr/bin/python3
"""Pascal Triangle"""
def pascal_triangle(n):
    """ Returns a pascal's triange"""
    if n <= 0:
        return []

    pascal = [[1]]  # Always starts with 1

    for i in range(1, n):
        previous = pascal[i - 1]
        current_row = [1]  # Each row starts and ends with 1

        """ calculate the pascal's triangle """
        for j in range(1, i):
            value = previous[j - 1] + previous[j]
            current_row.append(value)

        current_row.append(1)  # End the row with 1
        pascal.append(current_row)

    return pascal