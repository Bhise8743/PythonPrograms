import importlib
import pytest

module = importlib.import_module("Code.Simple_Calculator_Using_Functions")


def test_addition():
    assert module.add(10, 5) == 15


def test_subtraction():
    assert module.subtract(10, 5) == 5


def test_multiplication():
    assert module.multiply(10, 5) == 50


def test_division():
    assert module.divide(10, 5) == 2


def test_calculator_addition():
    assert module.calculate(10, 5, "+") == 15


def test_calculator_subtraction():
    assert module.calculate(10, 5, "-") == 5


def test_calculator_multiplication():
    assert module.calculate(10, 5, "*") == 50


def test_calculator_division():
    assert module.calculate(10, 5, "/") == 2


def test_division_by_zero():
    with pytest.raises(ValueError):
        module.divide(10, 0)


def test_invalid_operator():
    with pytest.raises(ValueError):
        module.calculate(10, 5, "%")
        
# python -m pytest .\Test_Code\Test_Simple_Calculator_Using_Functions.py