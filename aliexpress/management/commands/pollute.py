from django.core.management.base import BaseCommand, CommandError
from aliexpress import models


class Command(BaseCommand):  # Simple command for data polluting

    help = 'Populate database'

    def handle(self, *args, **options):

        product_rate = models.Rate(rate=9)
        product_rate.save()

        product_category = models.Category(category='Books')
        product_category.save()

        new_product = models.Product(name='Magazine', description="The new 'Forbs' magazine", rate=product_rate,
                       category=product_category)
        new_product.save()

        self.stdout.write(self.style.SUCCESS('Successfully populate data'))

