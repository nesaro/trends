from django.db import models
from django.contrib.auth.models import User
from aliexpress.utils import send_email


class Rate(models.Model):

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

    rate = models.ForeignKey(Rate, models.CASCADE)

    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return str(self.name)


class Price(models.Model):

    price = models.DecimalField(decimal_places=2, max_digits=9999999)

    created_at = models.DateTimeField()

    product = models.ForeignKey(Product, models.CASCADE)

    __original_price = None

    def __str__(self):
        return str(self.created_at)

    def __init__(self, *args, **kwargs):
        super(Price, self).__init__(*args, **kwargs)
        self.__original_price = self.price

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.price != self.__original_price:
            if TrackedListModel.objects.get(product_id=self.product_id):
                send_email('example@domain.com')  # REPLACE IS REQUIRED!

        super(Price, self).save(force_insert, force_update, using, update_fields)
        self.__original_price = self.price


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

    class Meta:
        verbose_name = 'Tracked List'
        verbose_name_plural = 'Tracked Lists'
