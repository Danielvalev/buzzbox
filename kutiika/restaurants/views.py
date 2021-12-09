from django.shortcuts import render
from .models import Restaurant, Menu, Dish
from datetime import date
import csv
from django.http import HttpResponseRedirect, HttpResponse, FileResponse


# Create your views here.
def restaurant_dashboard(request):
    return render(request, 'restaurants/dashboard.html')


def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants_list.html', {
        'restaurants': restaurants,
    })


def restaurants_menu(request, restaurant_id=1):
    today = str(date.today())
    year, month, day = today.split('-')

    # menus = Menu.objects.filter(restaurant_menu=restaurant_id).order_by('-menu_date')[:1]  # Show latest menu by date
    menus = Menu.objects.filter(restaurant_menu=restaurant_id, menu_date__year=year, menu_date__month=month,
                                menu_date__day=day)  # Show today menu

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


# Generate CSV File Menu
def menu_csv(request, restaurant_id):
    # Designate The Model
    today = str(date.today())
    year, month, day = today.split('-')

    filename = f'menu_{day}_{month}_{year}'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={filename}.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # menus = Menu.objects.filter(restaurant_menu=restaurant_id).order_by('-menu_date')[:1]  # Show latest menu by date
    menus = Menu.objects.filter(restaurant_menu=restaurant_id, menu_date__year=year, menu_date__month=month,
                                menu_date__day=day)  # Show today menu

    # Add column headings to the csv file
    writer.writerow(['Menu Date', 'Dish Name', 'Dish Category', 'Restaurant', 'Portion Size', 'Price'])

    # Loop Thu and output
    for menu in menus:
        for dish in menu.dish_menu.all():
            writer.writerow([menu.menu_date, dish.name, dish.food_category, dish.restaurant_dish,
                             dish.portion_size, dish.price])

    return response
