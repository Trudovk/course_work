import datetime
from django.shortcuts import render
from course_work.models import Category, Item, Review
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ItemSerializer, CategorySerializer, ReviewSerializer
from collections import OrderedDict
from rest_framework import filters
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

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
    pagination_class = AdvicePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        return Item.objects.filter(~Q(price=0) | ~Q(stock=0))
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_slug = request.query_params.get('category', None)
        if category_slug is not None:
            items = Item.objects.filter(category__slug=category_slug)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Category parameter is required"}, status=400)


class ItemUrlViewSet(viewsets.ModelViewSet):
    """
    API с товарами по ссылке на категорию /api/catalog/{slug}/
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Item.objects.filter(category__slug=slug)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API c категориями
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API с отзывами
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = AdvicePagination

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        comment = request.data.get('comment')
        customer = request.data.get('customer')
        rating = request.data.get('rating')

        if not comment or not customer or not rating:
            return Response({'status': 'Comment, customer name and rating are required'}, status=400)

        review = self.get_object()
        review.description = comment
        review.customer = customer
        review.rating = rating
        review.save()

        return Response({'status': 'Comment added'})


class TodayFiveStarsComentsViewSet(viewsets.ModelViewSet):
    """
    API с отзывами с рейтингом 5 за сегодня c содержанием /api/today_five_stars_coments
    """
    queryset = Review.objects.filter()
    serializer_class = ReviewSerializer


    def get_queryset(self):
        return Review.objects.filter(Q(review_date__gte=datetime.date.today()) & Q(rating=5) & ~Q(description='')) 
    # что то хорошее придумаю позже

class ItemReviewViewSet(viewsets.ModelViewSet):
    """
    API Опционально ограничивает возвращаемые отзывы до заданного товара и рейтинга,
    фильтруя по параметрам `item_id` и `rating` в URL. /api/item_reviews?rating=5&item_id=1
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        item_id = self.request.query_params.get('item_id')
        rating = self.request.query_params.get('rating')
        if item_id is not None:
            queryset = queryset.filter(product__id=item_id)
        if rating is not None:
            queryset = queryset.filter(rating=rating)
        return queryset