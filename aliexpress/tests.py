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

    def test_pollute_Product_model(self):
        self.assertTrue(self.product)
        self.assertIsNone(self.product.save())

    def test_pollute_Rate_model(self):
        self.assertTrue(self.rate)
        self.assertIsNone(self.rate.save())

    def test_pollute_Category_model(self):
        self.assertTrue(self.category)
        self.assertIsNone(self.category.save())

    def test_pollute_Price_model(self):
        self.assertTrue(self.price)
        self.assertIsNone(self.price.save())

    # def test_pollute_Image_model(self):
    #     new_one = models.Image(image=Image.open(os.path.join(
    #         settings.BASE_DIR, r'aliexpress/for_test/waterfall-wallpaper-13.jpg')))
    #     self.assertTrue(new_one)
    #     self.assertIsNone(new_one.save())
