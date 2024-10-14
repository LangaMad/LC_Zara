from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/home.html'

class FaqsView(TemplateView):
    template_name = 'pages/faqs.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class CheckoutView(TemplateView):
    template_name = 'pages/checkout.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'