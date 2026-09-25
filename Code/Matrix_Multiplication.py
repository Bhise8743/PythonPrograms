def matrix_multiplication(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")

    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Invalid matrix dimensions")

    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix2[0])):
            total = 0

            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    print(matrix_multiplication(matrix1, matrix2))
    
# python .\Code\Matrix_Multiplication.py