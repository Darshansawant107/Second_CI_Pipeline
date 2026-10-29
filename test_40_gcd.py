import importlib

module = importlib.import_module("40_gcd")


def test_gcd_common_factors():
    assert module.gcd(12, 8) == 4


def test_gcd_coprime_numbers():
    assert module.gcd(7, 3) == 1


def test_gcd_with_zero():
    assert module.gcd(10, 0) == 10


def test_gcd_negative_number():
    assert module.gcd(-12, 8) == 4