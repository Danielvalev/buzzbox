from django.shortcuts import render
from .models import Restaurant, Menu, Dish


# Create your views here.
def restaurant_dashboard(request):
    return render(request, 'restaurants/dashboard.html')


def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants_list.html', {
        'restaurants': restaurants,
    })


def restaurants_menu(request):
    menus = Menu.objects.all()

    # TODO Create a better sorting function
    # Sorting Dishes
    soups = []
    salads = []
    main_dishes = []
    desserts = []
    other_dishes = []

    for menu in menus:
        for dish in menu.dish_menu.all():
            dish_category = str(dish.food_category).strip()
            if dish_category.lower() == 'soups':
                soups.append(dish)
            if dish_category.lower() == 'salads':
                salads.append(dish)
            if dish_category.lower() == 'main':
                main_dishes.append(dish)
            if dish_category.lower() == 'desserts':
                desserts.append(dish)
            if dish_category.lower() == 'others':
                other_dishes.append(dish)

    return render(request, 'restaurants/restaurant_menu.html', {
        'menus': menus,
        'soups': soups,
        'salads': salads,
        'main_dishes': main_dishes,
        'desserts': desserts,
        'other_dishes': other_dishes,
    })
