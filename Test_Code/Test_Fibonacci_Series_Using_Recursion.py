import importlib
import pytest

module = importlib.import_module("Code.Fibonacci_Series_Using_Recursion")


def test_fibonacci_zero():
    assert module.fibonacci_recursive(0) == 0


def test_fibonacci_one():
    assert module.fibonacci_recursive(1) == 1


def test_fibonacci_five():
    assert module.fibonacci_recursive(5) == 5


def test_fibonacci_ten():
    assert module.fibonacci_recursive(10) == 55


def test_fibonacci_series():
    assert module.fibonacci_series(7) == [
        0, 1, 1, 2, 3, 5, 8
    ]


def test_negative_number():
    with pytest.raises(ValueError):
        module.fibonacci_recursive(-1)
        
