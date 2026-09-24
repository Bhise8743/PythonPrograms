import importlib

module = importlib.import_module("Code.Find_Sum_of_Digits")


def test_sum_of_digits():
    assert module.sum_of_digits(12345) == 15


def test_single_digit():
    assert module.sum_of_digits(7) == 7


def test_zero():
    assert module.sum_of_digits(0) == 0


def test_negative_number():
    assert module.sum_of_digits(-123) == 6


def test_number_with_zero():
    assert module.sum_of_digits(1020) == 3
    
    