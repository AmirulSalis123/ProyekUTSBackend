from django.contrib import admin
from .models import Category, Supplier, Item

# Mendaftarkan model Category
admin.site.register(Category)

# Mendaftarkan model Supplier
admin.site.register(Supplier)

# Mendaftarkan model Item
admin.site.register(Item)
