from django.core.management.base import BaseCommand
from aliexpress import models
from aliexpress.utils import string_generator, back_to
import random


class Command(BaseCommand):  # Simple command for data populating

    help = 'Populate database'

    def handle(self, *args, **options):

        categories_number = 20
        products_for_category = 100
        products_number = categories_number * products_for_category

        categories = [string_generator(10) for _ in range(categories_number)]

        category_objects = models.Category.objects.bulk_create(
            [models.Category(category=categories[product-1]) for product in range(categories_number)]
        )

        self.stdout.write('Categories are created')

        rate_objects = models.Rating.objects.bulk_create(
            [models.Rating(rate=random.randint(0, 10)) for _ in range(10)]
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
                                    rate=choose_rate(), category=category) for p in range(products_for_category)])

            for product in category.product_set.all():

                how_many_products += 1

                price_objects = models.Price.objects.bulk_create(
                    [models.Price(product=product,
                                  created_at=back_to(how_many_days_ago), price=random.randint(0, 10000))
                     for how_many_days_ago in range(200)]
                )

                self.stdout.write('Product %s, Category: %s Number: %s of %s' %
                                  (product, category, how_many_products, products_number))

        self.stdout.write(self.style.SUCCESS('Successfully populate data'))
