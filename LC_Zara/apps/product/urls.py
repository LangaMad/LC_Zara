<<<<<<< HEAD
from django.shortcuts import render, redirect


from .views import TestProductListView
from django.urls import path

urlpatterns = [
    path('api/v1/products/', TestProductListView.as_view(), name='products'),
]
=======
from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/products/' , ProductListCreateApiView.as_view(), name='products'),
    path('api/v1/products/<int:pk>/', ProductDetailApiView.as_view(), name='product'),
    path('api/v1/products/create/', ProductCreateApiView.as_view(), name='product-create'),
    path('api/v1/products/<int:pk>/update/', ProductUpdateApiView.as_view(), name='product-update'),
    path('api/v1/products/<int:pk>/delete/', ProductDeleteApiView.as_view(), name='product-delete'),

]
>>>>>>> 77f08be8cec50379e7cb9f08a7aeb7e2118530d4
