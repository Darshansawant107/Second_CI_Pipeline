import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating():
    assert module.first_non_repeating("swiss") == "w"


def test_no_non_repeating():
    assert module.first_non_repeating("aabbcc") is None


def test_single_character():
    assert module.first_non_repeating("a") == "a"