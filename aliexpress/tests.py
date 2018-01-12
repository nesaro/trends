from django.test import TestCase
from aliexpress import models
from django.utils import timezone


class AliExpressModelsTesting(TestCase):

    def setUp(self):
        self.rate = models.Rate(rate=9.6)
        self.rate.save()

        self.category = models.Category(category='Books')
        self.category.save()

        self.product = models.Product(name='Gold', description="Scrooge McDuck's gold",
                                      rate=self.rate,
                                      category=self.category)
        self.product.save()

        self.price = models.Price(price=676.50, created_at=timezone.now(), product=self.product)
        self.price.save()

    def test_creating_models(self):
        self.assertTrue(self.rate)
        self.assertTrue(self.category)
        self.assertTrue(self.product)
        self.assertTrue(self.price)


class CommandTesting(TestCase):

    def test_command(self):
        from django.core.management import call_command

        call_command('pollute')
