from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_customer, name='login'),
    path('logout/', views.logout_customer, name='logout'),
    path('register/', views.register_customer, name='register'),
]
