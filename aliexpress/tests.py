from django.test import TestCase
from aliexpress import models
from django.utils import timezone

# from PIL import Image
# from trends import settings
# import os.path


class AliexpressModelsTesting(TestCase):

    def setUp(self):
        self.rate = models.Rate(rate=9.6)
        self.rate_saving = self.rate.save()

        self.category = models.Category(category='Books')
        self.category_saving = self.category.save()

        self.product = models.Product(name='Gold', description="Scrooge McDuck's gold",
                                      rate=self.rate,
                                      category=self.category)
        self.product_saving = self.product.save()

        self.price = models.Price(price=676.50, created_at=timezone.now(), product=self.product)
        self.price_saving = self.price.save()

    def test_creating_models(self):
        self.assertTrue(self.rate)
        self.assertTrue(self.category)
        self.assertTrue(self.product)
        self.assertTrue(self.price)

    def test_saving_entries(self):
        self.assertIsNone(self.rate_saving)
        self.assertIsNone(self.category_saving)
        self.assertIsNone(self.product_saving)
        self.assertIsNone(self.price_saving)
