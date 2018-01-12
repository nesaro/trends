from django.core.management.base import BaseCommand
from aliexpress import models
from aliexpress.utils import string_generator, back_to
import random


class Command(BaseCommand):  # Simple command for data populating

    help = 'Populate database'

    def handle(self, *args, **options):

        CATEGORIES_NUMBER = 20
        PRODUCTS_FOR_CATEGORY = 100
        PRODUCTS_NUMBER = CATEGORIES_NUMBER * PRODUCTS_FOR_CATEGORY

        categories = [string_generator(10) for word in range(CATEGORIES_NUMBER)]

        category_objects = models.Category.objects.bulk_create(
            [models.Category(category=categories[product-1]) for product in range(CATEGORIES_NUMBER)]
        )

        self.stdout.write('Categories are created')

        rate_objects = models.Rate.objects.bulk_create(
            [models.Rate(rate=random.randint(0, 10)) for r in range(10)]
        )

        self.stdout.write('Rate objects are created')

        how_many_products = 0

        def choose_rate():
            choosen_rate = random.choice(rate_objects)
            choosen_rate.save()

            return choosen_rate

        for category in category_objects:
            category.save()

            product_objects = models.Product.objects.bulk_create(
                [models.Product(name=string_generator(12), description=string_generator(54),
                                    rate=choose_rate(), category=category) for p in range(PRODUCTS_FOR_CATEGORY)])

            for product in category.product_set.all():

                how_many_products += 1

                price_objects = models.Price.objects.bulk_create(
                    [models.Price(product=product, created_at=back_to(how_many_days_ago), price=random.randint(0, 10000))
                     for how_many_days_ago in range(200)]
                )

                self.stdout.write('Product %s, Category: %s Number: %s of %s' %
                                  (product, category, how_many_products, PRODUCTS_NUMBER))

        self.stdout.write(self.style.SUCCESS('Successfully populate data'))
