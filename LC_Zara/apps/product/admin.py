from django.contrib import admin
from .models import (
    TestProduct, TestCategory, Category, Subcategory, Color, Fabric, Brand, Country,
    ClothesSize, Clothes, ShoeSize, Shoes, Accessory, ClothImages, ShoeImages, AccessoryImages)


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = [ 'name','description']

@admin.register(TestProduct)
class TestProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',  'description',
        'price', 'stock', 'available',
        ]

class ClothImagesInline(admin.TabularInline):
    model = ClothImages
    extra = 1

class ShoeImagesInline(admin.TabularInline):
    model = ShoeImages
    extra = 1

class AccessoryImagesInline(admin.TabularInline):
    model = AccessoryImages
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ClothesSize)
class ClothesSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    search_fields = ('size',)

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'quantity', 'subcategory')
    search_fields = ('title', 'price')
    list_filter = ('subcategory', 'gender', 'available')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ClothImagesInline]

@admin.register(ShoeSize)
class ShoeSizeAdmin(admin.ModelAdmin):
    list_display = ('EUSize', 'USSize', 'CM')
    search_fields = ('EUSize', 'USSize')

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'quantity', 'subcategory')
    search_fields = ('title', 'price')
    list_filter = ('subcategory', 'gender', 'available')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ShoeImagesInline]

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'quantity', 'subcategory')
    search_fields = ('title', 'price')
    list_filter = ('subcategory', 'gender', 'available')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AccessoryImagesInline]



