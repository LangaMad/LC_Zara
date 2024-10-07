from django.shortcuts import render
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = 'pages/home.html'


class ProductsView(TemplateView):
    template_name = 'pages/products.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class FAQsView(TemplateView):
    template_name = 'pages/faqs.html'


class CheckoutView(TemplateView):
    template_name = 'pages/checkout.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class ShoppingcartView(TemplateView):
    template_name = 'pages/shoppingcart.html'



