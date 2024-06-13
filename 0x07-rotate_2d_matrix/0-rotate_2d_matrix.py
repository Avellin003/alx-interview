#!/usr/bin/python3
"""matrices 2D"""


def rotate_2d_matrix(matrix):
    """rotation 90 of the matrix"""
    left_s, right_s = 0, len(matrix) - 1

    while left_s < right_s:
        for a in range(right_s - left_s):
            # swapping
            up, bottom = left_s, right_s
            # Topleft value
            TopLeft = matrix[up][left_s + a]
            # bottom
            matrix[up][left_s + a] = matrix[bottom - a][left_s]
            # save to up
            matrix[bottom - a][left_s] = matrix[bottom][right_s - i]
            # right
            matrix[bottom][right_s - a] = matrix[up + a][right_s]
            # left to Top
            matrix[up + a][right_s] = TopLeft
        right_s -= 1
        left_s += 1
