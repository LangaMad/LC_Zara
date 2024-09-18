from django.urls import path , include
from .views import *

from rest_framework import routers

# routers 
router = routers.DefaultRouter()
# Viewsets
router.register(r'products', ProductViewSet)



urlpatterns = [
    path('api/v1/', include(router.urls)),

    # auth 
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # generics
    # path('api/v1/products/<int:pk>/', ProductDetailApiView.as_view(), name='product'),
    # path('api/v1/products/create/', ProductCreateApiView.as_view(), name='product-create'),
    # path('api/v1/products/<int:pk>/update/', ProductUpdateApiView.as_view(), name='product-update'),
    # path('api/v1/products/<int:pk>/delete/', ProductDeleteApiView.as_view(), name='product-delete'),

    # # Retrievs
    # path('api/v1/products/<int:pk>/', ProductRetrieveUpdateAPIView.as_view(), name='product-retrieve-update'),
    # path('api/v1/products/<int:pk>/', ProductRetrieveDestroyAPIView.as_view(), name='product-retrieve-destroy'),
    # path('api/v1/products/<int:pk>/', ProductProductRetrieveDestroyAPIView.as_view(), name='product-product-retrieve-destroy'),


]

