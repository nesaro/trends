from django.contrib import admin
from aliexpress import models as ali_models
from aliexpress import models


class ImagesInlineModel(admin.StackedInline):

    model = models.Image

    extra = 1


class PriceInlineModel(admin.TabularInline):

    model = models.Price
    extra = 1


class ProductAdminModel(admin.ModelAdmin):

    fieldsets = [

        ('Main info', {'fields': ['name', 'description', 'category']}),

    ]

    inlines = [ImagesInlineModel, PriceInlineModel]


admin.site.register(ali_models.Price)
admin.site.register(ali_models.Image)
admin.site.register(ali_models.Product, ProductAdminModel)
admin.site.register(ali_models.Rate)
admin.site.register(models.Category)
