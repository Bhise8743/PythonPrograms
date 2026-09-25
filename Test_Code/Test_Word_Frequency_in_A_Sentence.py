import importlib

module = importlib.import_module("Code.Word_Frequency_in_A_Sentence")


def test_word_frequency():
    assert module.word_frequency(
        "hello world hello"
    ) == {
        "hello": 2,
        "world": 1
    }


def test_single_word():
    assert module.word_frequency("hello") == {
        "hello": 1
    }


def test_empty_sentence():
    assert module.word_frequency("") == {}


def test_case_insensitive():
    assert module.word_frequency(
        "Hello hello HELLO"
    ) == {
        "hello": 3
    }


def test_multiple_words():
    assert module.word_frequency(
        "python is easy python is powerful"
    ) == {
        "python": 2,
        "is": 2,
        "easy": 1,
        "powerful": 1
    }
    
# python -m pytest .\Test_Code\Test_Word_Frequency_in_A_Sentence.py
