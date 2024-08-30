from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestProduct
        fields = ['id','name','description','price','stock','available']
