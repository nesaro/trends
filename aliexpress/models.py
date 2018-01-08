from django.db import models


class Rate(models.Model):

    rate = models.IntegerField()


class Category(models.Model):

    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Product(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    rate = models.ForeignKey(Rate)

    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Price(models.Model):

    price = models.DecimalField(decimal_places=3, max_digits=9999999)

    created_at = models.DateTimeField()

    product = models.ForeignKey(Product)


class Image(models.Model):

    image = models.ImageField()

    product = models.ForeignKey(Product)

    def __str__(self):
        return self.image.name
