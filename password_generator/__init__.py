from string import (
    ascii_lowercase as lower,
    ascii_uppercase as upper,
    digits,
    punctuation as symbols
)
from random import randint, shuffle

CHAR_LISTS = {
    'lower': lower,
    'upper': upper,
    'digits': digits,
    'symbols': symbols,
}

DEFAULT_OPTIONS = [
    'lower',
    'upper',
    'digits',
    'symbols',
]

def generate_password(length = 16, options = DEFAULT_OPTIONS):
    password = ''
    chars = []

    # GET VALID CHARACTERS
    for char_type in options:
        char_list = CHAR_LISTS.get(char_type)
        chars += char_list

        password += char_list[randint(0, len(char_list) - 1)]

    for _ in range(length - len(password)):
        password += chars[randint(0, len(chars) - 1)]

    password_list = list(password)
    shuffle(password_list)

    return ''.join(password_list)
