import importlib
import pytest

module = importlib.import_module("Code.Find_Second_Largest_Number_in_A_List")


def test_second_largest():
    assert module.second_largest([10, 20, 30, 40]) == 30


def test_unsorted_list():
    assert module.second_largest([50, 10, 30, 20]) == 30


def test_duplicate_values():
    assert module.second_largest([10, 20, 20, 30]) == 20


def test_negative_numbers():
    assert module.second_largest([-10, -5, -20]) == -10


def test_not_enough_unique_numbers():
    with pytest.raises(ValueError):
        module.second_largest([5, 5, 5])
        
#  python -m pytest .\Test_Code\Test_Fibonacci_Series.py
