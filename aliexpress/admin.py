from django.contrib import admin
from aliexpress import models


class ImagesInlineModel(admin.StackedInline):

    model = models.Image

    extra = 1


class PriceInlineModel(admin.TabularInline):

    model = models.Price
    extra = 1


class ProductAdminModel(admin.ModelAdmin):

    fieldsets = [

        ('Main info', {'fields': ['name', 'description', 'category', 'rate']}),

    ]

    list_display = ['name', 'category', 'rate']

    inlines = [ImagesInlineModel, PriceInlineModel]


admin.site.register(models.Price)
admin.site.register(models.Image)
admin.site.register(models.Product, ProductAdminModel)
admin.site.register(models.Rate)
admin.site.register(models.Category)
admin.site.register(models.TrackedList)
