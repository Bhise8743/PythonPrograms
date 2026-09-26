import importlib

module = importlib.import_module("Code.Merge_Two_Sorted_Lists")


def test_merge_lists():
    assert module.merge_sorted_lists(
        [1, 3, 5],
        [2, 4, 6]
    ) == [1, 2, 3, 4, 5, 6]


def test_first_list_empty():
    assert module.merge_sorted_lists(
        [],
        [1, 2, 3]
    ) == [1, 2, 3]


def test_second_list_empty():
    assert module.merge_sorted_lists(
        [1, 2, 3],
        []
    ) == [1, 2, 3]


def test_both_empty():
    assert module.merge_sorted_lists([], []) == []


def test_duplicates():
    assert module.merge_sorted_lists(
        [1, 2, 2],
        [2, 3, 3]
    ) == [1, 2, 2, 2, 3, 3]


def test_negative_numbers():
    assert module.merge_sorted_lists(
        [-5, -2],
        [-4, 0]
    ) == [-5, -4, -2, 0]
    
