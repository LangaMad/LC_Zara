from django.contrib import admin
from .models import TestProduct

# Register your models here.

@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',  'description',
        'price', 'stock', 'available',

        ]
@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',  'description',
        'price', 'stock', 'available',
        ]
