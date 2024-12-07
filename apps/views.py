from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [HasAPIKey]
