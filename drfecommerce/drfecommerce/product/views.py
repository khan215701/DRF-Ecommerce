from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category
# Create your views here.


class CategoryView(viewsets.ViewSet):
    """
    using viewsets to listing categories
    """
    queryset = Category.objects.all()
    
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many = True)
        return Response(serializer.data)
    


