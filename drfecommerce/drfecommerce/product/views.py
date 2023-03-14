from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
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
    


