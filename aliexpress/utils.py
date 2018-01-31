import random
from string import ascii_letters
from django.utils import timezone
from django.core import mail


def string_generator(max_length):

    length = random.randint(1, abs(max_length))

    word = ''

    for _ in range(length):
        word += random.choice(ascii_letters)

    return word


def back_to(days_count):
    the_day = timezone.now() - timezone.timedelta(days=days_count)
    return the_day


def send_email(*recipients):
    mail.send_mail('Subscription',
                   "Hello! Your tracked product's price has been changed.",
                   'amazon.aliexpress@bk.ru',
                   recipients,
                   fail_silently=True,)

    return 'Success!'
