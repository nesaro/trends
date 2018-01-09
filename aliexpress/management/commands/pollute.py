from django.core.management.base import BaseCommand, CommandError
from aliexpress import models


class Command(BaseCommand):  # Simple command for data polluting

    help = 'Populate database'

    def handle(self, *args, **options):

        self.product_rate = models.Rate(rate=9)
        self.product_rate.save()

        self.product_category = models.Category(category='Books')
        self.product_category.save()

        self.new_product = models.Product(name='Magazine', description="The new 'Forbs' magazine", rate=self.product_rate,
                       category=self.product_category)
        self.new_product.save()

        self.stdout.write(self.style.SUCCESS('Successfully populate data'))
