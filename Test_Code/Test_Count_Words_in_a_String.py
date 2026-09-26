import importlib

module = importlib.import_module("Code.Count_Words_in_a_String")


def test_simple_sentence():
    assert module.count_words("Hello world") == 2


def test_multiple_words():
    assert module.count_words(
        "Python is easy to learn"
    ) == 5


def test_empty_string():
    assert module.count_words("") == 0


def test_extra_spaces():
    assert module.count_words(
        "  Hello   world  "
    ) == 2


def test_single_word():
    assert module.count_words("Python") == 1
    
# python -m pytest .\Test_Code\Test_Count_Words_in_a_String.py
