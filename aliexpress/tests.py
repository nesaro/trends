from django.test import TestCase
from aliexpress import models
from django.utils import timezone

# from PIL import Image
# from trends import settings
# import os.path


class AliexpressModelsTesting(TestCase):

    def setUp(self):
        self.rate = models.Rate(rate=9.6)
        self.category = models.Category(category='Books')
        self.product = models.Product(name='Gold', description="Scrooge McDuck's gold",
                                      rate=self.rate,
                                      category=self.category)
        self.price = models.Price(price=676.50, created_at=timezone.now(), product=self.product)

    def saving_entries(self):
        self.assertIsNone(self.rate.save())
        self.assertIsNone(self.category.save())
        self.assertIsNone(self.product.save())
        self.assertIsNone(self.price.save())

