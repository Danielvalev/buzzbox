from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.restaurant_dashboard, name='restaurant-dashboard'),
]
