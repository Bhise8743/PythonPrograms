def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ValueError("Matrices must have the same dimensions")

    if any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same dimensions")

    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    print(matrix_addition(matrix1, matrix2))
    
