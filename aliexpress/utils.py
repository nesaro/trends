import random
from string import ascii_letters


def string_generator(max_length):

    length = random.randint(1, abs(max_length))

    word = ''

    for w in range(length):
        word += random.choice(ascii_letters)

    return word
