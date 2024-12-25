from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey
from .models import Product
from .serializers import ProductSerializer
from .models import User
from .serializers import UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [HasAPIKey]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [HasAPIKey]
