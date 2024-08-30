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
