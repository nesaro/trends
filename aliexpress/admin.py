from django.contrib import admin
from aliexpress import models as ali_models

admin.site.register(ali_models.Price)
admin.site.register(ali_models.Image)
admin.site.register(ali_models.Product)
admin.site.register(ali_models.Rate)
