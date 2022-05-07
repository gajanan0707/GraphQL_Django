from django.contrib import admin

from .models import Category, Book, Grocery

# Register your models here.

# Registering the models with the admin site.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Grocery)
