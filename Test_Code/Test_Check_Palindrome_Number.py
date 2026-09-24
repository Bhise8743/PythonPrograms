import importlib

module = importlib.import_module("Code.Check_Palindrome_Number")


def test_palindrome():
    assert module.is_palindrome(121) is True


def test_another_palindrome():
    assert module.is_palindrome(12321) is True


def test_not_palindrome():
    assert module.is_palindrome(123) is False


def test_zero():
    assert module.is_palindrome(0) is True


def test_negative_number():
    assert module.is_palindrome(-121) is False
    
    
# python -m pytest .\Test_Code\Test_Check_Palindrome_Number.py