from django.core.management.base import BaseCommand, CommandError
from aliexpress import models
from aliexpress.utils import string_generator, back_to
import random
from django.utils import timezone


class Command(BaseCommand):  # Simple command for data polluting

    help = 'Populate database'

    def handle(self, *args, **options):

        CATEGORIES_NUMBER = 20
        PRODUCTS_NUMBER = 100

        categories = [string_generator(10) for word in range(CATEGORIES_NUMBER)]

        category_objects = models.Category.objects.bulk_create(
            [models.Category(category=categories[product-1]) for product in range(CATEGORIES_NUMBER)]
        )

        self.stdout.write('Categories are created')

        rate_objects = models.Rate.objects.bulk_create(
            [models.Rate(rate=random.randint(0, 10)) for r in range(10)]
        )

        self.stdout.write('Rate objects are created')

        how_many = 0

        for categ in category_objects:
            categ.save()

            choosen_rate = random.choice(rate_objects)
            choosen_rate.save()

            product_objects = models.Product.objects.bulk_create(
                [models.Product(name=string_generator(12), description=string_generator(54),
                                    rate=choosen_rate, category=categ) for p in range(PRODUCTS_NUMBER)])
            for prod in product_objects:
                prod.save()

                price_objects = models.Price.objects.bulk_create(
                    [models.Price(product=prod, created_at=back_to(how_many), price=random.randint(0, 10000))
                     for how_many in range(200)]
                )
                self.stdout.write('Product %s, Category: %s' % (prod, categ))

        self.stdout.write(self.style.SUCCESS('Successfully populate data'))
