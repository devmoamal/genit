
import random

def str(length, add_characters = "") -> str:

    characters = "abcdefghijklmnopqrstuvwxyz" + add_characters

    random_str = ""

    for i in range(length):
        random_str = "{}{}".format(random_str, characters[random.randint(0, len(characters) - 1)])

    return random_str

def int(length) -> int:

    characters = "1234567890"

    random_int = ""

    for i in range(length):
        random_int = "{}{}".format(random_int, characters[random.randint(0, len(characters) - 1)])

    return int(random_int)

def all(length, add_characters = "") -> str:

    characters = "abcdefghijklmnopqrstuvwxyz1234567890" + add_characters

    random_str = ""

    for i in range(length):
        random_str = "{}{}".format(random_str, characters[random.randint(0, len(characters) - 1)])

    return random_str

def special(length, characters) -> str:

    characters = "" + characters
    random_str = ""

    for i in range(length):
        random_str = "{}{}".format(random_str, characters[random.randint(0, len(characters) - 1)])

    return random_str
