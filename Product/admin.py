from django.contrib import admin

# Register your models here.
from Product.models import shop, product, category
admin.site.register(shop)
admin.site.register(product)
admin.site.register(category)
