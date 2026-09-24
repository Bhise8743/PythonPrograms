import importlib

module = importlib.import_module("Code.Largest_Of_Three_Num")


def test_largest_first():
    assert module.largest_of_three(10, 5, 3) == 10


def test_largest_second():
    assert module.largest_of_three(2, 15, 7) == 15


def test_largest_third():
    assert module.largest_of_three(2, 5, 20) == 20


def test_all_equal():
    assert module.largest_of_three(5, 5, 5) == 5


def test_negative_numbers():
    assert module.largest_of_three(-10, -5, -20) == -5
    
# python -m pytest Test_Code\Test_Largest_Of_Three_Num.py
