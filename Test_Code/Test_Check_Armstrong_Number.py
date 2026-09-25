import importlib

module = importlib.import_module("Code.Check_Armstrong_Number")


def test_armstrong_153():
    assert module.is_armstrong(153) is True


def test_armstrong_370():
    assert module.is_armstrong(370) is True


def test_armstrong_9474():
    assert module.is_armstrong(9474) is True


def test_not_armstrong():
    assert module.is_armstrong(123) is False


def test_zero():
    assert module.is_armstrong(0) is True


def test_negative_number():
    assert module.is_armstrong(-153) is False
    
# python -m pytest .\Test_Code\Test_Check_Armstrong_Number.py