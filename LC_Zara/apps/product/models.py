from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('Slug', unique=True)
    photo = models.ImageField('Фотография', upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField('Название подкатегории', max_length=100)
    slug = models.SlugField('Slug', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    photo = models.ImageField('Фотография', upload_to='subcategories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

class Gender(models.TextChoices):
    MALE = 'M', 'Мужской'
    FEMALE = 'F', 'Женский'
    UNISEX = 'U', 'Унисекс'

class Color(models.Model):
    name = models.CharField('Название цвета', max_length=150)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

class Fabric(models.Model):
    name = models.CharField('Название материала', max_length=150)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField('Название бренда', max_length=200)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField('Страна производитель')

    class Meta:
        verbose_name = 'Страна производитель'
        verbose_name_plural = 'Страны производители'

class ClothesSize(models.TextChoices):
    XS = 'XS', 'Экстра маленький'
    S = 'S', 'Маленький'
    M = 'M', 'Средний'
    L = 'L', 'Большой'
    XL = 'XL', 'Экстра большой'

class Clothes(models.Model):
    title = models.CharField('Название одежды', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    size = models.CharField('Размер', max_length=2, choices=ClothesSize.choices)
    gender = models.CharField('Пол', max_length=1, choices=Gender.choices, default=Gender.UNISEX)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='clothes')
    photo = models.ImageField('Фотография', upload_to='clothes/', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return self.title

class ShoeSize(models.Model):
    size = models.CharField('Размер обуви', max_length=10)

    class Meta:
        verbose_name = 'Размер обуви'
        verbose_name_plural = 'Размеры обуви'

    def __str__(self):
        return self.size

class Shoe(models.Model):
    title = models.CharField('Название обуви', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    size = models.ForeignKey(ShoeSize, on_delete=models.SET_NULL, null=True, verbose_name='Размер')
    gender = models.CharField('Пол', max_length=1, choices=Gender.choices, default=Gender.UNISEX)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
    material = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='shoes')
    photo = models.ImageField('Фотография', upload_to='shoes/', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'

    def __str__(self):
        return self.title

class Accessory(models.Model):
    title = models.CharField('Название аксессуара', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    gender = models.CharField('Пол', max_length=1, choices=Gender.choices, default=Gender.UNISEX)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
    material = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='accessories')
    photo = models.ImageField('Фотография', upload_to='accessories/', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
        ordering = ['title']

    def __str__(self):
        return self.title
