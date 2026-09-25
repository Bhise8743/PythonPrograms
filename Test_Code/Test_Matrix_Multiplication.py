import importlib
import pytest

module = importlib.import_module("Code.Matrix_Multiplication")


def test_2x2_multiplication():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    assert module.matrix_multiplication(matrix1, matrix2) == [
        [19, 22],
        [43, 50]
    ]


def test_identity_matrix():
    matrix = [[1, 2], [3, 4]]
    identity = [[1, 0], [0, 1]]

    assert module.matrix_multiplication(matrix, identity) == matrix


def test_zero_matrix():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[0, 0], [0, 0]]

    assert module.matrix_multiplication(matrix1, matrix2) == [
        [0, 0],
        [0, 0]
    ]


def test_rectangular_matrices():
    matrix1 = [[1, 2, 3]]
    matrix2 = [[4], [5], [6]]

    assert module.matrix_multiplication(matrix1, matrix2) == [[32]]


def test_invalid_dimensions():
    with pytest.raises(ValueError):
        module.matrix_multiplication(
            [[1, 2]],
            [[1, 2]]
        )
        
# python -m pytest .\Test_Code\Test_Matrix_Multiplication.py