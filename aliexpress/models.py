from django.db import models


class Price(models.Model):

    price = models.IntegerField(max_length=999999)


class Rate(models.Model):

    rate = models.IntegerField(max_length=100)


class Images(models.Model):

    images = models.ImageField()


class Goods(models.Model):

    name = models.CharField(max_length=200)

    category = models.CharField(max_length=200)

    description = models.CharField(max_length=1000)

    images = models.ForeignKey(Images)

    rate = models.ForeignKey(Rate)

    price = models.ForeignKey(Price)
