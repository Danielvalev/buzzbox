from django.contrib import admin
from .models import Restaurant, FoodCategory, Dish

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(FoodCategory)
admin.site.register(Dish)

# TODO add more filters to Dish and Restaurant
