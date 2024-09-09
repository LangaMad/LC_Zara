from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TestProduct
from .serializers import TestProductSerializer




class TestProductListView(APIView):
    def get(self, request):
        posts = TestProduct.objects.all().values()
        return Response({'posts': list(posts)})
#         products = TestProduct.objects.all()
#         serializer = TestProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        new_product = TestProduct.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price'],
            stock=request.data['stock'],
        )
        return Response({'post': model_to_dict(new_product)})
#         serializer = TestProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.generics import ListCreateAPIView

# class TestProductListCreateView(ListCreateAPIView):
#     queryset = TestProduct.objects.all()
#     serializer_class = TestProductSerializer