from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.restaurant_dashboard, name='restaurant-dashboard'),
    path('', views.restaurants_list, name='restaurants-list'),
    path('menu/<restaurant_id>/', views.restaurants_menu, name='restaurant-menu'),
    path('menu_csv/<restaurant_id>/', views.menu_csv, name='menu-csv'),
]
