from django.db import models
from django.contrib.auth.models import User


class Rate(models.Model):

    rate = models.IntegerField()

    def __str__(self):
        return str(self.rate)


class Category(models.Model):

    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Product(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    rate = models.ForeignKey(Rate, models.CASCADE)

    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return str(self.name)


class Price(models.Model):

    price = models.DecimalField(decimal_places=2, max_digits=9999999)

    created_at = models.DateTimeField()

    product = models.ForeignKey(Product, models.CASCADE)

    def __str__(self):
        return str(self.created_at)


class Image(models.Model):

    image = models.ImageField()

    product = models.ForeignKey(Product, models.CASCADE)

    def __str__(self):
        return self.image.name
