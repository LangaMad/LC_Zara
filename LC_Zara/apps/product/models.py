from django.db import models

from django.db import models


class TestProduct(models.Model):
    name = models.CharField('Название', max_length=200) # подгузник
    description = models.TextField('Описание', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Количество на складе', null = True, blank = True)
    available = models.BooleanField('В наличии', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name












# class Category(models.Model):
#     name = models.CharField('Название категории', max_length=100)
#     slug = models.SlugField('Slug', unique=True)
#     photo = models.ImageField('Фотография', upload_to='categories/', blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name
#
# class Subcategory(models.Model):
#     name = models.CharField('Название подкатегории', max_length=100)
#     slug = models.SlugField('Slug', unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
#     photo = models.ImageField('Фотография', upload_to='subcategories/', blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Подкатегория'
#         verbose_name_plural = 'Подкатегории'
#
#     def __str__(self):
#         return self.name
#
# class Color(models.Model):
#     name = models.CharField('Название цвета', max_length=150)
#
#     class Meta:
#         verbose_name = 'Цвет'
#         verbose_name_plural = 'Цвета'
#
#     def __str__(self):
#         return self.name
#
# class Fabric(models.Model):
#     name = models.CharField('Название материала', max_length=150)
#
#     class Meta:
#         verbose_name = 'Материал'
#         verbose_name_plural = 'Материалы'
#
#     def __str__(self):
#         return self.name
#
# class Brand(models.Model):
#     name = models.CharField('Название бренда', max_length=200)
#     logo = models.ImageField('Лого', upload_to='logo/')
#
#     class Meta:
#         verbose_name = 'Бренд'
#         verbose_name_plural = 'Бренды'
#
#     def __str__(self):
#         return self.name
#
# class Country(models.Model):
#     name = models.CharField('Страна производитель')
#
#     class Meta:
#         verbose_name = 'Страна производитель'
#         verbose_name_plural = 'Страны производители'
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     PRODUCT_TYPE_CHOICES = (
#         ('clothes', 'Clothes'),
#         ('trousers', 'Trousers'),
#         ('shoe', 'Shoe'),
#         ('accessory', 'Accessory'),
#     )
#
#     GENDER_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('unisex', 'Unisex')
#     )
#
#     title = models.CharField('Название', max_length=200)
#     description = models.TextField('Описание', blank=True, null=True)
#     gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES, default='unisex')
#     color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
#     material = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
#     price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
#     available = models.BooleanField('В наличии', default=True)
#     quantity = models.IntegerField('Количество', default=0)
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
#     photo = models.ImageField('Фотография', upload_to='products/', blank=True, null=True)
#     slug = models.SlugField('Slug', unique=True)
#     product_type = models.CharField('Тип продукта', max_length=10, choices=PRODUCT_TYPE_CHOICES)
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#         ordering = ['title']
#
#     def __str__(self):
#         return f"{self.get_product_type_display()} - {self.title}"
#
# class Clothes(Product):
#     CLOTHES_SIZE_CHOICE = (
#         ('XS', 'Extra small'),
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#         ('XL', 'Extra large'),
#         ('XXL', 'Double extra large')
#     )
#
#     clothes_size = models.CharField('Размер', max_length=3, choices=CLOTHES_SIZE_CHOICE)
#
#     class Meta:
#         verbose_name = 'Одежда'
#         verbose_name_plural = 'Одежда'
#
#     def __str__(self):
#         return self.title
#
# class Trousers(Product):
#     WAIST_SIZES = (
#         ('28', '28'),
#         ('30', '30'),
#         ('32', '32'),
#         ('34', '34'),
#         ('36', '36'),
#         ('38', '38'),
#         ('40', '40'),
#     )
#     LENGTH_SIZES = (
#         ('30', '30'),
#         ('32', '32'),
#         ('34', '34'),
#         ('36', '36'),
#     )
#
#     waist_size = models.CharField('Обхват талии', max_length=2, choices=WAIST_SIZES)
#     length_size = models.CharField('Длина брюк', max_length=2, choices=LENGTH_SIZES)
#
#     class Meta:
#         verbose_name = 'Брюки'
#         verbose_name_plural = 'Брюки'
#
#     def __str__(self):
#         return self.title
#
# class Shoes(Product):
#     EUROPEAN_SIZES = (
#         ('35', '35'),
#         ('36', '36'),
#         ('37', '37'),
#         ('38', '38'),
#         ('39', '39'),
#         ('40', '40'),
#         ('41', '41'),
#         ('42', '42'),
#         ('43', '43'),
#         ('44', '44'),
#         ('45', '45'),
#     )
#
#     US_SIZES = (
#         ('5', '5'),
#         ('6', '6'),
#         ('7', '7'),
#         ('8', '8'),
#         ('9', '9'),
#         ('10', '10'),
#         ('11', '11'),
#         ('12', '12'),
#     )
#
#     size_eu = models.CharField('Размер (Европейский)', max_length=2, choices=EUROPEAN_SIZES, blank=True, null=True)
#     size_us = models.CharField('Размер (Американский)', max_length=2, choices=US_SIZES, blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Обувь'
#         verbose_name_plural = 'Обувь'
#
#     def __str__(self):
#         return self.title
#
# class Accessory(Product):
#     class Meta:
#         verbose_name = 'Аксессуар'
#         verbose_name_plural = 'Аксессуары'
#         ordering = ['title']
#
#     def __str__(self):
#         return self.title
#
#
#
