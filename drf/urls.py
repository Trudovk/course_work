from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'reviews', views.ReviewViewSet)
# router.register

urlpatterns = [
    path('api/', include(router.urls)),
    re_path(r'api/catalog/(?P<slug>.+)/$', views.ItemUrlViewSet.as_view({'get': 'list'})),
    re_path(r'api/today_five_stars_coments', views.TodayFiveStarsComentsViewSet.as_view({'get': 'list'})),
    re_path(r'api/item_reviews', views.ItemReviewViewSet.as_view({'get': 'list'})),
    re_path(r'api/special', views.ItemSpecialViewSet.as_view({'get': 'list'})),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]