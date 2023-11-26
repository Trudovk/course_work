from django.shortcuts import render
from course_work.models import Category, Item
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ItemSerializer, CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API с товарами
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API c категориями
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    