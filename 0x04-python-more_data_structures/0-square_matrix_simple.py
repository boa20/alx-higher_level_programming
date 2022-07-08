#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in matrix:
        square = []
        for j in i:
            square.append(j**2)
        squares.append(square)
    return squares
