import importlib

module = importlib.import_module("37_fibonacci")


def test_fibonacci_five_terms():
    assert module.fibonacci(5) == [0, 1, 1, 2, 3]


def test_fibonacci_seven_terms():
    assert module.fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_zero_terms():
    assert module.fibonacci(0) == []