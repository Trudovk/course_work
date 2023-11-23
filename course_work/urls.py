from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('catalog/', views.categories, name='catalog'),
    path('catalog/<str:category>/', views.catalog, name='category'),
    path('i/<int:item_id>/', views.item, name='item'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart_in_cart/<int:item_id>/', views.add_to_cart_in_cart, name='add_to_cart_in_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/remove_from_cart_in_cart/<int:item_id>/', views.remove_from_cart_in_cart, name='remove_from_cart_in_cart'),
    path('cart/remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
