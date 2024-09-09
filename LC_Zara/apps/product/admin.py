from django.contrib import admin
from .models import TestProduct

# Register your models here.

@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['id', 'name', 'description', 'price', 'stock', 'available']
=======
    list_display = [
        'id', 'name',  'description',
        'price', 'stock', 'available',
        ]
>>>>>>> 77f08be8cec50379e7cb9f08a7aeb7e2118530d4
