import random


def string_generator(max_length):
    alphabet = ('a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y',
                          'z')
    length = random.randint(1, abs(max_length))

    word = ''

    for w in range(length):
        word += random.choice(alphabet)

    return word
