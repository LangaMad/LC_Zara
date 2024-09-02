from PIL.ImImagePlugin import number
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django import forms
from django.db.models import ManyToManyField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    second_name = models.CharField('Отчество', max_length=50)
    email = models.EmailField('Почта', unique=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', null=True, blank=True)
    phone_number = models.IntegerField('Номер тел.', max_length=15)
    gender = forms.ChoiceField('Пол', choices=GENDER_CHOICES)
    favorite_brand = models.ManyToManyField('Лучший бренд', max_length=50)
    favorite_product = models.ManyToManyField('Лучший продукт', max_length=50)

    objects = UserManager()


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


#
 # Balance model
class Balance(models.Model):
    user = models.OneToOneField('Пользователь', User, on_delete=models.CASCADE)
    amount = models.DecimalField('Текущий баланс', max_digits=10, decimal_places=2, default=0.00)
    email = models.EmailField('Почта', unique=True)
    gift_certificate = models.CharField('Подарочный сертификат', max_length=50)
    last_updated = models.DateTimeField('Последнее обновление', auto_now=True)
    popolnit_balans = models.IntegerField('Пополнить баланс', auto_now=True)

    def __str__(self):
        return f"Balance for {self.user.email}: {self.amount}"
        return f"last_updated for {self.user.email}: {self.amount}"


    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'



# Payment Method model
class PaymentMethod(models.Model):
    CARD_TYPE_CHOICES = [
        ('MBANK', 'MBANK'),
        ('Optima Bank', 'Optima Bank'),
    ]
    email = models.EmailField('Почта', unique=True)
    user = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE, related_name='payment_methods')
    method_name = models.CharField('Имя способа оплаты', max_length=50)
    card_number = models.CharField('Номер карты', max_length=20)  # Simplified card number storage
    tri_sifry_na_oborotke_karty = models.IntegerField('ТРи цифры на оборотке карты', max_length=3)
    сard_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES, default='credit')

    def __str__(self):
        return f"{self.user.email} - {self.method_name}"


    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'




# Installment model
class Rassrochka(models.Model):
    user = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE, related_name='Rassrochki')
    email = models.EmailField('Почта', unique=True)
    amount = models.DecimalField('Текущий баланс', max_digits=10, decimal_places=2)
    due_date = models.DateField('Срок оплаты', auto_now=True)
    paid = models.BooleanField('Оплачено', default=False)

    def __str__(self):
        return f"Rassrochka for {self.user.email} - Amount: {self.amount}, Due: {self.due_date}"

    class Meta:
        verbose_name = 'Rassrochka'
        verbose_name_plural = 'Rassrochki'




# Receipt model
class Chek(models.Model):
    user = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE, related_name='Cheki')
    amount = models.DecimalField('Текущий баланс', max_digits=10, decimal_places=2)
    date = models.DateField('Дата', auto_now=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return f"Chek for {self.user.email} - Amount: {self.amount}, Date: {self.date}"

    class Meta:
        verbose_name = 'Chek'
        verbose_name_plural = 'Cheki'



# Purchase model
class Pokupka(models.Model):
    user = models.ForeignKey('Пользователь', User, on_delete=models.CASCADE, related_name='Pokupki')
    product_name = models.CharField('Название продукта', max_length=100)
    amount = models.DecimalField('Текущий баланс', max_digits=10, decimal_places=2)
    Pokupka_date = models.DateField('День покупки',  auto_now=True)

    def __str__(self):
        return f"Pokupka by {self.user.email} - product: {self.product_name}, Amount: {self.amount}"

    class Meta:
        verbose_name = 'Pokupka'
        verbose_name_plural = 'Pokupki'
