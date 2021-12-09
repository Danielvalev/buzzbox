from django.contrib import admin
from .models import Restaurant, FoodCategory, Dish, Menu

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(FoodCategory)
admin.site.register(Menu)


# admin.site.register(Dish)

# TODO add more filter to Restaurant
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    fields = ('name', 'portion_size', 'price', 'restaurant_dish', 'food_category')
    list_display = ('name', 'food_category', 'restaurant_dish', 'price')
    list_filter = ('restaurant_dish', 'food_category')
    ordering = ('restaurant_dish',)


