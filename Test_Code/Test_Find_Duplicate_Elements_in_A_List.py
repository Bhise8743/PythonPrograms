import importlib

module = importlib.import_module("Code.Find_Duplicate_Elements_in_A_List")


def test_duplicates():
    assert module.find_duplicates([1, 2, 2, 3, 3, 4]) == [2, 3]


def test_no_duplicates():
    assert module.find_duplicates([1, 2, 3, 4]) == []


def test_multiple_duplicates():
    assert module.find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]


def test_empty_list():
    assert module.find_duplicates([]) == []


def test_same_number_multiple_times():
    assert module.find_duplicates([5, 5, 5, 5]) == [5]
    
# python -m pytest .\Test_Code\Test_Find_Duplicate_Elements_in_A_List.py