import importlib

module = importlib.import_module("32_anagram")


def test_anagrams_true():
    assert module.are_anagrams("listen", "silent") is True


def test_anagrams_false():
    assert module.are_anagrams("hello", "world") is False


def test_anagrams_ignore_case_and_spaces():
    assert module.are_anagrams("Dormitory", "Dirty room") is True