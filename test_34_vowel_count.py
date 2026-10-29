import importlib

module = importlib.import_module("34_vowel_count")


def test_count_vowels():
    assert module.count_vowels("hello") == 2


def test_count_vowels_uppercase():
    assert module.count_vowels("Education") == 5


def test_count_no_vowels():
    assert module.count_vowels("sky") == 0