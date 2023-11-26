from django.shortcuts import render
from course_work.models import Category, Item
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ItemSerializer, CategorySerializer
from collections import OrderedDict

class AdvicePagination(PageNumberPagination):
    page_size = 5
    page_sizer_query_param = 'paginate_by'
    max_page_size = 20

class ItemViewSet(viewsets.ModelViewSet):
    """
    API с товарами
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = AdvicePagination

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API c категориями
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    