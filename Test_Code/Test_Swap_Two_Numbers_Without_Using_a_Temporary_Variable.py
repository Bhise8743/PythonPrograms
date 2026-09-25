import importlib

module = importlib.import_module("Code.Swap_Two_Numbers_Without_Using_a_Temporary_Variable")


def test_swap():
    assert module.swap_numbers(10, 20) == (20, 10)


def test_swap_negative_numbers():
    assert module.swap_numbers(-5, -10) == (-10, -5)


def test_swap_with_zero():
    assert module.swap_numbers(0, 10) == (10, 0)


def test_same_numbers():
    assert module.swap_numbers(5, 5) == (5, 5)


def test_decimal_numbers():
    assert module.swap_numbers(2.5, 5.5) == (5.5, 2.5)
    
# python -m pytest .\Test_Code\Test_Swap_Two_Numbers_Without_Using_a_Temporary_Variable.py