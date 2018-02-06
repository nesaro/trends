import random
from string import ascii_letters
from django.utils import timezone
from django.core import mail
from trends.settings import EMAIL_SUBJECT, EMAIL_TEXT, EMAIL_HOST_USER


def string_generator(max_length):

    length = random.randint(1, abs(max_length))

    word = ''

    for _ in range(length):
        word += random.choice(ascii_letters)

    return word


def back_to(days_count):
    return timezone.now() - timezone.timedelta(days=days_count)


def send_email(*recipients):
    mail.send_mail(EMAIL_SUBJECT,
                   EMAIL_TEXT,
                   EMAIL_HOST_USER,
                   recipients,
                   fail_silently=False)

    return 'Success!'
