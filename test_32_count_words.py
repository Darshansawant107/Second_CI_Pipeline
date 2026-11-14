import importlib

module = importlib.import_module("32_count_words")


def test_count_words():
    assert module.count_words("Hello World") == 2


def test_empty_sentence():
    assert module.count_words("") == 0


def test_multiple_spaces():
    assert module.count_words("Python is very easy") == 4