# from PIL.ImImagePlugin import number
# from django.db import models
#
# # Create your models here.
# from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,User
# from django import forms

#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(email, password, **extra_fields)
#
#
# class User(AbstractUser):
#     GENDER_CHOICES = [
#         ('male', 'male'),
#         ('female', 'female'),
#     ]
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     second_name = models.CharField(max_length=50)
#     email = models.EmailField('Почта', unique=True)
#     avatar = models.ImageField('Аватар', upload_to='avatars/', null=True, blank=True)
#     number = models.IntegerField()
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)
#     favorite_brand = models.CharField(max_length=50)
#     favorite_product = models.CharField(max_length=50)
#     objects = UserManager()
#
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#
#
#
# # Balance model
# class Balance(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#
#     def __str__(self):
#         return f"Balance for {self.user.email}: {self.amount}"
#
#     class Meta:
#         verbose_name = 'Balance'
#         verbose_name_plural = 'Balances'
#
# # Payment Method model
# class PaymentMethod(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_methods')
#     method_name = models.CharField(max_length=50)
#     card_number = models.CharField(max_length=20)  # Simplified card number storage
#
#     def __str__(self):
#         return f"{self.user.email} - {self.method_name}"
#
#     class Meta:
#         verbose_name = 'Payment Method'
#         verbose_name_plural = 'Payment Methods'
#
#
# # Installment model
# class Installment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='installments')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     due_date = models.DateField()
#     paid = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"Installment for {self.user.email} - Amount: {self.amount}, Due: {self.due_date}"
#
#     class Meta:
#         verbose_name = 'Installment'
#         verbose_name_plural = 'Installments'
#
# # Receipt model
# class Receipt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receipts')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()
#     description = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"Receipt for {self.user.email} - Amount: {self.amount}, Date: {self.date}"
#
#     class Meta:
#         verbose_name = 'Receipt'
#         verbose_name_plural = 'Receipts'
#
# # Purchase model
# class Purchase(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
#     item_name = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     purchase_date = models.DateField()
#
#     def __str__(self):
#         return f"Purchase by {self.user.email} - Item: {self.item_name}, Amount: {self.amount}"
#
#     class Meta:
#         verbose_name = 'Purchase'
#         verbose_name_plural = 'Purchases'
#
# # Favorite Brand model
# class FavoriteBrand(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_brands')
#     brand_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.user.email} - {self.brand_name}"
# # hello
#
#     class Meta:
#         verbose_name = 'Favorite Brand'
#         verbose_name_plural = 'Favorite Brands'
#
# # Favorite Item model
# class FavoriteItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_items')
#     item_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.user.email} - {self.item_name}"
#
#     class Meta:
#         verbose_name = 'Favorite Item'
#         verbose_name_plural = 'Favorite Items'
