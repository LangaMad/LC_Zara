from django.db import models



class TestCategory(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class TestProduct(models.Model):
    name = models.CharField('Название', max_length=200) # подгузник
    description = models.TextField('Описание', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Количество на складе', null = True, blank = True)
    available = models.BooleanField('В наличии', default=True)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE,
                                 related_name='products', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name







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
    description = models.TextField('Описание бренда')
    logo = models.ImageField('Лого бренда', upload_to='logos/')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField('Страна производитель')
    flag = models.ImageField('Флаг страны', upload_to='flags/')

    class Meta:
        verbose_name = 'Страна производитель'
        verbose_name_plural = 'Страны производители'

    def __str__(self):
        return self.name

class ClothesSize(models.Model):
    size = models.CharField('Размер одежды', max_length=20)

    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежды'

    def __str__(self):
        return self.size


class Clothes(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('unisex', 'unisex'),
    ]

    title = models.CharField('Название одежды', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    size = models.ForeignKey(ClothesSize, on_delete=models.CASCADE, verbose_name='Размер')
    gender = models.CharField('Пол', choices=GENDER_CHOICES, default='unisex')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('В наличии', default=True)
    quantity = models.IntegerField('Количество', default=0)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='clothes')
    photo = models.ImageField('Фотография', upload_to='clothes/', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return self.title

class ClothImages(models.Model):
    cloth = models.ForeignKey(Clothes, related_name='clothes_image', verbose_name='Фото одежды', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='clothes/')

    class Meta:
        verbose_name = 'Изображение одежды'
        verbose_name_plural = 'Изображения одежды'

    def __str__(self):
        return f"Изображение для {self.cloth.title}"

class ShoeSize(models.Model):
    EUSize = models.CharField('Европейский размер', max_length=10)
    USSize = models.CharField('Американский размер', max_length=10)
    CM = models.PositiveIntegerField('Сантиметр')

    class Meta:
        verbose_name = 'Размер обуви'
        verbose_name_plural = 'Размеры обуви'

    def __str__(self):
        return f"EU: {self.EUSize}, US: {self.USSize}, {self.CM} cm"

class Shoes(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('unisex', 'unisex'),
    ]

    title = models.CharField('Название обуви', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    size = models.ForeignKey(ShoeSize, on_delete=models.CASCADE, null=True, verbose_name='Размер обуви')
    gender = models.CharField(choices=GENDER_CHOICES, default='unisex')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('В наличии', default=True)
    quantity = models.IntegerField('Количество', default=0)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='shoes')
    photo = models.ImageField('Фотография', upload_to='shoes/', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'

    def __str__(self):
        return self.title

class ShoeImages(models.Model):
    shoe = models.ForeignKey(Shoes, related_name='shoes_image', verbose_name='Фото обуви', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='shoes/')

    class Meta:
        verbose_name = 'Изображение обуви'
        verbose_name_plural = 'Изображения обуви'

    def __str__(self):
        return f"Изображение для {self.shoe.title}"
class Accessory(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('unisex', 'unisex'),
    ]

    title = models.CharField('Название аксессуара', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    gender = models.CharField('Пол', choices=GENDER_CHOICES, default='unisex')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Цвет')
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, verbose_name='Материал')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name='Бренд')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна производитель')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('В наличии', default=True)
    quantity = models.IntegerField('Количество', default=0)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='accessories')
    photo = models.ImageField('Фотография', upload_to='accessories/', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
        ordering = ['title']

    def __str__(self):
        return self.title

class AccessoryImages(models.Model):
    accessory = models.ForeignKey(Accessory, related_name='accessory_image', verbose_name='Фото аксессуара', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='accessories/')

    class Meta:
        verbose_name = 'Изображение акссесуара'
        verbose_name_plural = 'Изображения акссесуаров'

    def __str__(self):
        return f"Изображение для {self.accessory.title}"


