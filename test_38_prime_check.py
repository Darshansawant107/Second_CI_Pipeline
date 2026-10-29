import importlib

module = importlib.import_module("38_prime_check")


def test_prime_number():
    assert module.is_prime(7) is True


def test_composite_number():
    assert module.is_prime(10) is False


def test_number_less_than_two():
    assert module.is_prime(1) is False
    assert module.is_prime(0) is False
    assert module.is_prime(-5) is False
