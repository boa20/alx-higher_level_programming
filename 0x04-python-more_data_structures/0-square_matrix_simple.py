#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in matrix:
        square = []
        for j in i:
            square.append(j**2)
        squares.append(square)
    return squares

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
