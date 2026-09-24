import importlib

module = importlib.import_module("Code.Remove_Duplicates_from_A_List")


def test_remove_duplicates():
    assert module.remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]


def test_no_duplicates():
    assert module.remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_all_duplicates():
    assert module.remove_duplicates([5, 5, 5, 5]) == [5]


def test_empty_list():
    assert module.remove_duplicates([]) == []


def test_preserves_order():
    assert module.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    
# python -m pytest .\Test_Code\Test_Remove_Duplicates_from_A_List.py
