from django.contrib import admin

# Register your models here.
from Store.models import Category,Brand,Size,Product,Order

admin.site.register(Category)

admin.site.register(Brand)

admin.site.register(Size)

admin.site.register(Product)

admin.site.register(Order)
