import random
from string import ascii_letters
from django.utils import timezone


def string_generator(max_length):

    length = random.randint(1, abs(max_length))

    word = ''

    for w in range(length):
        word += random.choice(ascii_letters)

    return word


def back_to(days_count):
    the_day = timezone.now() - timezone.timedelta(days=days_count)
    return the_day
