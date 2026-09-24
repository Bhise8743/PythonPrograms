import importlib

module = importlib.import_module("Code.Reverse_A_String")


def test_reverse_string():
    assert module.reverse_string("hello") == "olleh"


def test_single_character():
    assert module.reverse_string("a") == "a"


def test_empty_string():
    assert module.reverse_string("") == ""


def test_string_with_spaces():
    assert module.reverse_string("hello world") == "dlrow olleh"


def test_numbers_as_string():
    assert module.reverse_string("12345") == "54321"
    
# python -m pytest .\Test_Code\Test_Reverse_A_String.py