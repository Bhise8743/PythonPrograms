import importlib
import pytest

module = importlib.import_module("Code.Calculate_Factorial")


def test_factorial_zero():
    assert module.factorial(0) == 1


def test_factorial_one():
    assert module.factorial(1) == 1


def test_factorial_five():
    assert module.factorial(5) == 120


def test_factorial_ten():
    assert module.factorial(10) == 3628800


def test_negative_number():
    with pytest.raises(ValueError):
        module.factorial(-5)
        
# python -m pytest .\Test_Code\Test_Calculate_Factorial.py
