from django.contrib import admin

from product import models

admin.site.register(models.Product)
admin.site.register(models.Subcategory)
admin.site.register(models.Category)
admin.site.register(models.Comment)
