from django.shortcuts import render
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics , viewsets , mixins
from .models import TestProduct,TestCategory
from .serializer import ProductSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
IsAdminUser,AllowAny,IsAuthenticated)
from .permissions import IsOwnerOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = TestCategory.objects.all().values()
        return Response({'cats': [cats]})

# Create your views here.

class ProductListApiView(generics.ListAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

class ProductCreateApiView(generics.CreateAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

# chop is dish
#
# peace do ball


# name = {'keys':{'asjfa':'data sdg'}}
#
# class ProductApiView(APIView):
#     def get(self, request):
#         posts = TestProduct.objects.all().values()
#         return Response({'posts': list(posts)})
#         # return Response({'message': 'Hello World'})
#         # products = Product.objects.all()
#         # serializer = ProductSerializer(products, many=True)
#         # return Response(serializer.data)
#
#     def post(self, request):
#         new_product = TestProduct.objects.create(
#             title=request.data['title'],
#             description=request.data['description'],
#             price=request.data['price'],
#             stock=request.data['stock'],
#         )
#         return Response({'post': model_to_dict(new_product)})
#         # return Response({'message': 'Hello World post'})
#     #     serializer = ProductSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#

# get - Получить данные
# post - Отправить данные
# put - Полное обновление данных
# patch - частичное обновление данных
# delete - Удалить данные
# head - Получить заголовки
# options - Получить доступные методы

