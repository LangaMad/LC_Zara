from django.shortcuts import render
from django_filters.filters import AllValuesFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestProduct
from django.forms.models import model_to_dict

# Create your views here.


class ProductApiView(APIView):
    def get(self, request):
        posts = TestProduct.objects.all().values()
        return Response({'posts': list(posts)})

    def post(self, request):
        new_product = TestProduct.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            price=request.data['price'],
            stock=request.data['stock'],
        )
        return Response({'post': model_to_dict(new_product)})