import importlib

module = importlib.import_module("Code.Find_Common_Elements_in_Two_Lists")


def test_common_elements():
    assert module.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_no_common_elements():
    assert module.common_elements([1, 2], [3, 4]) == []


def test_all_common():
    assert module.common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_duplicate_elements():
    assert module.common_elements([1, 1, 2, 2], [1, 2]) == [1, 2]


def test_empty_list():
    assert module.common_elements([], [1, 2]) == []
    
# python -m pytest .\Test_Code\Test_Find_Common_Elements_in_Two_Lists.py    
