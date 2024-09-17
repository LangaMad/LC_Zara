from django.contrib import admin
from .models import TestCategory, TestProduct

# Register your models here.

@admin.register(TestCategory)
class TestProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'stock', 'available']

