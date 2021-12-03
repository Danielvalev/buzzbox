from django.shortcuts import render
from .models import Restaurant


# Create your views here.
def restaurant_dashboard(request):
    return render(request, 'restaurants/dashboard.html')


def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants_list.html', {
        'restaurants': restaurants,
    })
