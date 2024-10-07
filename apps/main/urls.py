from django.urls import path
from . views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('about/', AboutView.as_view(), name='about'),
    path('faqs/', FAQsView.as_view(), name='faqs'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shoppingcart/', ShoppingcartView.as_view(), name='shoppingcart'),

]