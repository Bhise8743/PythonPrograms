import importlib
import pytest

module = importlib.import_module("Code.Factorial_Using_Recursion")


def test_factorial_zero():
    assert module.factorial_recursive(0) == 1


def test_factorial_one():
    assert module.factorial_recursive(1) == 1


def test_factorial_five():
    assert module.factorial_recursive(5) == 120


def test_factorial_ten():
    assert module.factorial_recursive(10) == 3628800


def test_negative_number():
    with pytest.raises(ValueError):
        module.factorial_recursive(-1)
        
# python -m pytest .\Test_Code\Test_Factorial_Using_Recursion.py