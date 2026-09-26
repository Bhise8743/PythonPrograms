import importlib

module = importlib.import_module("Code.Remove_Punctuation_from_a_String")


def test_remove_punctuation():
    assert module.remove_punctuation(
        "Hello, World!"
    ) == "Hello World"


def test_multiple_punctuation():
    assert module.remove_punctuation(
        "Hello!!! How are you???"
    ) == "Hello How are you"


def test_no_punctuation():
    assert module.remove_punctuation(
        "Hello World"
    ) == "Hello World"


def test_only_punctuation():
    assert module.remove_punctuation(
        "!@#$%"
    ) == ""


def test_empty_string():
    assert module.remove_punctuation("") == ""
    
# python -m pytest .\Test_Code\Test_Remove_Punctuation_from_a_String.py