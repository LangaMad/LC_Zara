from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TestProduct, TestCategory

# Register your models here.

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',  'description']


@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',  'description',
        'price', 'stock', 'available',

        ]