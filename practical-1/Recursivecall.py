def display(matrix, rows, cols, i, j):
    if i == rows:
        return

    print(matrix[i][j], end=" ")

    if j == cols - 1:
        print()
        display(matrix, rows, cols, i + 1, 0)
    else:
        display(matrix, rows, cols, i, j + 1)
