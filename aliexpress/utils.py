import random
from string import ascii_letters
import django.utils.timezone as t


def string_generator(max_length):

    length = random.randint(1, abs(max_length))

    word = ''

    for w in range(length):
        word += random.choice(ascii_letters)

    return word


def back_to(days_count):
    the_day = t.now() - t.timedelta(days=days_count)
    return the_day
