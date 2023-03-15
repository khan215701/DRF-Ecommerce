from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .models import Category, Brand, Product
from drf_spectacular.utils import extend_schema
# Create your views here.


class CategoryView(viewsets.ViewSet):
    """
    using viewsets to listing categories
    """
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many = True)
        return Response(serializer.data)
    

class BrandView(viewsets.ViewSet):
    """
    using viewsets to listing Brand
    """
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many = True)
        return Response(serializer.data)
    

class ProductView(viewsets.ViewSet):
    """
    using viewsets to listing Product
    """
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many = True)
        return Response(serializer.data)
    


