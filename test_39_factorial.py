import importlib

module = importlib.import_module("39_factorial")


def test_factorial_of_five():
    assert module.factorial(5) == 120


def test_factorial_of_three():
    assert module.factorial(3) == 6


def test_factorial_of_zero():
    assert module.factorial(0) == 1


def test_factorial_of_negative_number():
    try:
        module.factorial(-1)
    except ValueError:
        assert True
    else:
        assert False
    