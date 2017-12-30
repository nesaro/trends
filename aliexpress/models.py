from django.db import models


class Rate(models.Model):

    rate = models.IntegerField()


class Image(models.Model):

    image = models.ImageField()


class Price(models.Model):

    price = models.DecimalField(decimal_places=3, max_digits=9999999)

    date_time = models.DateTimeField()


class Category(models.Model):

    category = models.CharField(max_length=100)


class Product(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ForeignKey(Image)

    rate = models.ForeignKey(Rate)

    price = models.ForeignKey(Price)

    def __str__(self):
        return self.name
