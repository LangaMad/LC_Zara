# from django.urls import path , include,  re_path
# from .views import *
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from rest_framework_simplejwt.views import TokenVerifyView
#
#
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)
#
#
# urlpatterns = [
#     path('api/v1/', include(router.urls)),
#     path('api/v1/drf-auth/', include('rest_framework.urls')),
#     path('auth/', include('djoser.urls')),
#     re_path(r'^auth/', include('djoser.urls.authtoken')),
#     re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
#
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     # path('api/v1/products/<int:pk>/', ProductDetailApiView.as_view(), name='product'),
#     # path('api/v1/products/create-prod', ProductListCreateApiView.as_view(), name='product-create'),
#     # path('api/v1/products/<int:pk>/update/', ProductUpdateApiView.as_view(), name='product-update'),
#     # path('api/v1/products/<int:pk>/delete/', ProductDeleteApiView.as_view(), name='product-delete'),
#
# ]product-delete