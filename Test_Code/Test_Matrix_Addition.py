import importlib
import pytest

module = importlib.import_module("Code.Matrix_Addition")


def test_2x2_matrix():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    assert module.matrix_addition(matrix1, matrix2) == [
        [6, 8],
        [10, 12]
    ]


def test_3x3_matrix():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    assert module.matrix_addition(matrix1, matrix2) == [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10]
    ]


def test_zero_matrix():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[0, 0], [0, 0]]

    assert module.matrix_addition(matrix1, matrix2) == matrix1


def test_negative_values():
    assert module.matrix_addition(
        [[-1, -2]],
        [[1, 2]]
    ) == [[0, 0]]


def test_different_dimensions():
    with pytest.raises(ValueError):
        module.matrix_addition(
            [[1, 2]],
            [[1, 2], [3, 4]]
        )

# python -m pytest .\Test_Code\Test_Matrix_Addition.py