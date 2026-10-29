import importlib

module = importlib.import_module("36_reverse_string")


def test_reverse_string():
    assert module.reverse_string("hello") == "olleh"


def test_reverse_string_mixed_case():
    assert module.reverse_string("Python") == "nohtyP"


def test_reverse_empty_string():
    assert module.reverse_string("") == ""