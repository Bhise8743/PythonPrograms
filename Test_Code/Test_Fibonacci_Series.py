import importlib
import pytest

module = importlib.import_module("Code.Fibonacci_Series")


def test_zero_terms():
    assert module.fibonacci_series(0) == []


def test_one_term():
    assert module.fibonacci_series(1) == [0]


def test_five_terms():
    assert module.fibonacci_series(5) == [0, 1, 1, 2, 3]


def test_ten_terms():
    assert module.fibonacci_series(10) == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    ]


def test_negative_terms():
    with pytest.raises(ValueError):
        module.fibonacci_series(-1)
        
        
#  python -m pytest .\Test_Code\Test_Fibonacci_Series.py
