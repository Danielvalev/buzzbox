from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.restaurant_dashboard, name='restaurant-dashboard'),
    path('', views.restaurants_list, name='restaurants-list'),
    path('menu/', views.restaurants_menu, name='restaurant-menu'),
]
