from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):

    rate = models.IntegerField()

    def __str__(self):
        return str(self.rate)


class Category(models.Model):

    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    rate = models.ForeignKey(Rating, models.CASCADE)

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


class TrackedListModel(models.Model):

    user = models.ForeignKey(User, models.CASCADE)

    product = models.ForeignKey(Product, models.CASCADE)

    def __str__(self):
        return str(self.user)
