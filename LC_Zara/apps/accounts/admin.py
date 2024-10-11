# from django.contrib import admin
#
# # Register your models here.
#
# from django.contrib import admin
# from .models import User  # Ensure the import statement is correct
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'favorite_brand', 'favorite_product')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from django.contrib import admin
# from .models import User, Balance, PaymentMethod, Installment, Receipt, Purchase, FavoriteBrand, FavoriteItem
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'favorite_brand', 'favorite_product')
#     search_fields = ('first_name', 'last_name', 'email')
#     list_filter = ('gender',)
#     ordering = ('-date_joined',)
#     filter_horizontal = ()
#     fieldsets = (
#         (None, {'fields': ('first_name', 'last_name', 'second_name', 'email', 'avatar', 'phone_number', 'gender', 'favorite_brand', 'favorite_product')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
# class BalanceAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount')
#     search_fields = ('user_email',)
#     list_filter = ('user',)
#     ordering = ('-amount',)
#
# class PaymentMethodAdmin(admin.ModelAdmin):
#     list_display = ('user', 'method_name', 'card_number')
#     search_fields = ('user_email', 'method_name')
#     list_filter = ('user', 'method_name')
#
# class InstallmentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount', 'due_date', 'paid')
#     search_fields = ('user_email',)
#     list_filter = ('paid', 'due_date')
#     ordering = ('-due_date',)
#
# class ReceiptAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount', 'date', 'description')
#     search_fields = ('user_email', 'description')
#     list_filter = ('date',)
#     ordering = ('-date',)
#
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'item_name', 'amount', 'purchase_date')
#     search_fields = ('user_email', 'item_name')
#     list_filter = ('purchase_date',)
#     ordering = ('-purchase_date',)
#
# class FavoriteBrandAdmin(admin.ModelAdmin):
#     list_display = ('user', 'brand_name')
#     search_fields = ('user_email', 'brand_name')
#     list_filter = ('user',)
#
# class FavoriteItemAdmin(admin.ModelAdmin):
#     list_display = ('user', 'item_name')
#     search_fields = ('user_email', 'item_name')
#     list_filter = ('user',)
#
# # Register your models here.
# admin.site.register(User, UserAdmin)
# admin.site.register(Balance, BalanceAdmin)
# admin.site.register(PaymentMethod, PaymentMethodAdmin)
# admin.site.register(Installment, InstallmentAdmin)
# admin.site.register(Receipt, ReceiptAdmin)
# admin.site.register(Purchase, PurchaseAdmin)
# admin.site.register(FavoriteBrand, FavoriteBrandAdmin)
# admin.site.register(FavoriteItem, FavoriteItemAdmin)
