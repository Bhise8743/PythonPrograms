import importlib

module = importlib.import_module("Code.Check_Palindrome_String")


def test_palindrome():
    assert module.is_palindrome_string("madam") is True


def test_another_palindrome():
    assert module.is_palindrome_string("level") is True


def test_not_palindrome():
    assert module.is_palindrome_string("hello") is False


def test_uppercase_palindrome():
    assert module.is_palindrome_string("MADAM") is True


def test_empty_string():
    assert module.is_palindrome_string("") is True
    
# python -m pytest .\Test_Code\Test_Check_Palindrome_String.py
