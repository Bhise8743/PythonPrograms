import importlib

module = importlib.import_module("Code.Reverse_A_Number")


def test_reverse_number():
    assert module.reverse_number(12345) == 54321


def test_reverse_number_with_zero():
    assert module.reverse_number(1200) == 21


def test_single_digit():
    assert module.reverse_number(5) == 5


def test_zero():
    assert module.reverse_number(0) == 0


def test_negative_number():
    assert module.reverse_number(-123) == -321
    

# python -m pytest .\Test_Code\Test_Reverse_A_Number.py 