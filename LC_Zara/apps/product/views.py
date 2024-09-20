# from distutils.command.install import value
#
# from django.template.context_processors import request
# from django.template.defaultfilters import title
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# from .models import TestProduct
# from .serializers import TestProductSerializer
# from rest_framework.response import Response
# from .models import TestProduct
#
#
# class TestProductListView(APIView):
#     def get(self, request):
#         products = TestProduct.objects.all()
#         serializer = TestProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = TestProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ProductApiView(APIView):
#     def get(self, request):
#         posts = TestProduct.objects.all().values()
#         return Response({'posts': list(posts)})
#         # return Response({'massage': 'Hello world'})
#
#     def post(self, request):
#         new_product = TestProduct.objects.create(
#             title=request.data['title'],
#             description=request.data['description'],
#             price=request.data['price'],
#             stock=request(),
#         )
#         return Response({'massage': 'Hello world post'})


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestProduct, TestCategory
from rest_framework import generics, viewsets, mixins
# Create your views here.
from .serializers import ProductSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny,IsAuthenticated,)
from .permissions import IsOwnerOrReadOnly


#
#
# class ProductViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = TestProduct.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerOrReadOnly,)



    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = TestCategory.objects.all().values()
        return Response({'cats': [cats]})




class ProductListApiView(generics.ListAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

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


class ProductRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestProduct.objects.all()
    serializer_class = ProductSerializer


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
        # return Response({'message': 'Hello World post'})
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)