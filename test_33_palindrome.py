import importlib

module = importlib.import_module("33_palindrome")


def test_palindrome_true():
    assert module.is_palindrome("madam") is True


def test_palindrome_false():
    assert module.is_palindrome("hello") is False


def test_palindrome_ignore_spaces_and_case():
    assert module.is_palindrome("Nurses Run") is True