from django.core.management.base import BaseCommand, CommandError
from aliexpress import models
from aliexpress.utils import string_generator
import random
from django.utils import timezone


class Command(BaseCommand):  # Simple command for data polluting

    help = 'Populate database'

    def handle(self, *args, **options):

        CATEGORIES_COUNT = 20

        categories = [string_generator(10) for word in range(CATEGORIES_COUNT)]

        category_objects = models.Category.objects.bulk_create(
            [models.Category(category=categories[product-1]) for product in range(CATEGORIES_COUNT)]
        )

        self.stdout.write('Categories are created')

        rate_objects = models.Rate.objects.bulk_create(
            [models.Rate(rate=random.randint(0, 10)) for r in range(10)]
        )

        self.stdout.write('Rate objects are created')

        for categ in category_objects:
            categ.save()

            choosen_rate = random.choice(rate_objects)
            choosen_rate.save()

            product_objects = models.Product.objects.bulk_create(
                [models.Product(name=string_generator(12), description=string_generator(54),
                                    rate=choosen_rate, category=categ) for p in range(100)])

        self.stdout.write(self.style.SUCCESS('Successfully populate data'))
