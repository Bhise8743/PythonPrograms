import importlib

module = importlib.import_module("Code.Check_Perfect_Number")


def test_perfect_6():
    assert module.is_perfect(6) is True


def test_perfect_28():
    assert module.is_perfect(28) is True


def test_perfect_496():
    assert module.is_perfect(496) is True


def test_not_perfect():
    assert module.is_perfect(10) is False


def test_one():
    assert module.is_perfect(1) is False


def test_zero():
    assert module.is_perfect(0) is False
    
# python -m pytest .\Test_Code\Test_Check_Perfect_Number.py