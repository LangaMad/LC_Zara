from django.urls import path , include
from .views import *

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/products/<int:pk>/', ProductDetailApiView.as_view(), name='product'),
    # path('api/v1/products/create/', ProductCreateApiView.as_view(), name='product-create'),
    # path('api/v1/products/<int:pk>/update/', ProductUpdateApiView.as_view(), name='product-update'),
    # path('api/v1/products/<int:pk>/delete/', ProductDeleteApiView.as_view(), name='product-delete'),
    #
]
