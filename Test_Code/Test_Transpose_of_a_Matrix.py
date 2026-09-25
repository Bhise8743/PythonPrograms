import importlib

module = importlib.import_module("Code.Transpose_of_a_Matrix")


def test_2x3_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    assert module.transpose_matrix(matrix) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_square_matrix():
    matrix = [
        [1, 2],
        [3, 4]
    ]

    assert module.transpose_matrix(matrix) == [
        [1, 3],
        [2, 4]
    ]


def test_single_row():
    assert module.transpose_matrix([[1, 2, 3]]) == [
        [1],
        [2],
        [3]
    ]


def test_single_column():
    assert module.transpose_matrix([[1], [2], [3]]) == [
        [1, 2, 3]
    ]


def test_empty_matrix():
    assert module.transpose_matrix([]) == []
    
#  python -m pytest .\Test_Code\Test_Transpose_of_a_Matrix.py