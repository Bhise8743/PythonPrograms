import importlib

module = importlib.import_module("Code.Bubble_Sort_Implementation")


def test_unsorted_list():
    assert module.bubble_sort(
        [5, 2, 8, 1, 3]
    ) == [1, 2, 3, 5, 8]


def test_already_sorted():
    assert module.bubble_sort(
        [1, 2, 3, 4, 5]
    ) == [1, 2, 3, 4, 5]


def test_reverse_order():
    assert module.bubble_sort(
        [5, 4, 3, 2, 1]
    ) == [1, 2, 3, 4, 5]


def test_duplicates():
    assert module.bubble_sort(
        [3, 1, 2, 3, 1]
    ) == [1, 1, 2, 3, 3]


def test_empty_list():
    assert module.bubble_sort([]) == []


def test_original_list_unchanged():
    numbers = [3, 2, 1]

    module.bubble_sort(numbers)

    assert numbers == [3, 2, 1]
    
# python -m pytest .\Test_Code\Test_Bubble_Sort_Implementation.py