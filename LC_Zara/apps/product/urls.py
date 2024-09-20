# apps/product/urls.py
from django.urls import path
from . import views
#
# urlpatterns = [
#     # path('some-url/', views.some_view, name='some_view'),
#     # Add more URL patterns as needed
# ]
# from django.shortcuts import render, redirect
#
#
from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)



urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/products/', ProductViewSet.as_view({'get':'list'}), name='products'),
    # path('api/v1/products/<int:pk>/', ProductDetailApiView.as_view(), name='product'),
    # path('api/v1/products/create/', ProductCreateApiView.as_view(), name='product-create'),
    # path('api/v1/products/<int:pk>/update/', ProductUpdateApiView.as_view(), name='product-update'),
    # path('api/v1/products/<int:pk>/delete/', ProductDeleteApiView.as_view(), name='product-delete'),
    #
    # path('api/v1/products/RetrieveUpdate/', ProductRetrieveUpdateApiView.as_view(), name='product-RetrieveUpdate'),
    # path('api/v1/products/<int:pk>/RetrieveDestroy/', ProductRetrieveDestroyApiView.as_view(), name='product-RetrieveDestroy'),
    # path('api/v1/products/<int:pk>/RetrieveUpdateDestroy/', ProductRetrieveUpdateDestroyApiView.as_view(), name='product-RetrieveUpdateDestroy'),

]