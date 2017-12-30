from django.test import TestCase
from aliexpress import models
import datetime
from PIL import Image
from trends import settings
import os.path


class AliexpressModelsTesting(TestCase):

    def test_pollute_Product_model(self):
        new_one = models.Product(name='Gold', description="Scrooge McDuck's gold", rate=self.test_pollute_Rate_model())
        self.assertTrue(new_one)
        self.assertIsNone(new_one.save())
        return new_one

    def test_pollute_Rate_model(self):
        new_one = models.Rate(rate=9.6)
        self.assertTrue(new_one)
        self.assertIsNone(new_one.save())
        return new_one

    def test_pollute_Category(self):
        new_one = models.Category(category='Books')
        self.assertTrue(new_one)
        self.assertIsNone(new_one.save())
        return new_one

    def test_pollute_Price_model(self):
        new_one = models.Price(price=676.50, date_time=datetime.datetime.now(), product=self.test_pollute_Product_model())
        self.assertTrue(new_one)
        self.assertIsNone(new_one.save())
        return new_one

    # def test_pollute_Image_model(self):
    #     new_one = models.Image(image=Image.open(os.path.join(
    #         settings.BASE_DIR, r'aliexpress/for_test/waterfall-wallpaper-13.jpg')))
    #     self.assertTrue(new_one)
    #     self.assertIsNone(new_one.save())
