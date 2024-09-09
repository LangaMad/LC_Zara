from .models import TestProduct
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestProduct
        fields = [
            'id', 'name', 'description', 
            'price', 'stock', 'available'
        ]



