import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_zero_rotation():
    assert module.rotate_string("abcdef", 0) == "abcdef"


def test_full_rotation():
    assert module.rotate_string("abcdef", 6) == "abcdef"