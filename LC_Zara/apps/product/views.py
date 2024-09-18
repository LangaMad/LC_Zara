from django.shortcuts import render
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework.response import Response

from rest_framework import generics, viewsets, mixins
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import GenericViewSet

from .models import TestCategory, TestProduct
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer


from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import action


# Create your views here.

# class ProductListApiView(generics.ListAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailApiView(generics.RetrieveAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

# class ProductCreateApiView(generics.CreateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

# class ProductUpdateApiView(generics.UpdateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

# class ProductDeleteApiView(generics.DestroyAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

# class ProductListCreateApiView(generics.ListCreateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer


# Retrieves

# class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

# class ProductRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer


# class ProductProductRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'id'


# viewsets  
# + permission 

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    
    @action(methods=['get'], detail=False)
    def category(self, request, pk=None):
        cats = TestCategory.objects.all().values()
        return Response({'cats': cats})

    












