import string


def is_pangram(text):
    alphabet = set(string.ascii_lowercase)
    letters = set(text.lower())

    return alphabet.issubset(letters)