import importlib

module = importlib.import_module("35_word_count")


def test_count_words():
    assert module.count_words("Hello World") == 2


def test_count_multiple_words():
    assert module.count_words("Python is easy to learn") == 5


def test_count_empty_string():
    assert module.count_words("") == 0