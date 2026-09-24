import importlib

module = importlib.import_module("Code.Find_Missing_Number_in_A_List")


def test_missing_number():
    assert module.find_missing_number([1, 2, 3, 5]) == 4


def test_missing_first():
    assert module.find_missing_number([2, 3, 4, 5]) == 1


def test_missing_last():
    assert module.find_missing_number([1, 2, 3, 4]) == 5


def test_missing_middle():
    assert module.find_missing_number([1, 2, 4, 5, 6]) == 3


def test_small_list():
    assert module.find_missing_number([1]) == 2
    
# python -m pytest .\Test_Code\Test_Find_Missing_Number_in_A_List.py