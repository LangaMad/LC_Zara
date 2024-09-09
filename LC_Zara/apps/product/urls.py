from django.shortcuts import render, redirect


from .views import TestProductListView
from django.urls import path

urlpatterns = [
    path('api/v1/products/', TestProductListView.as_view(), name='products'),
]
