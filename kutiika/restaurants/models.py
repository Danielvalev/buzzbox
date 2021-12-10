from django.db import models
from django.db.models import PROTECT
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField('Restaurant Name', max_length=120)
    address = models.CharField(max_length=300)
    description = models.CharField('Description', max_length=255)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    logo = models.ImageField(upload_to='public/restaurant_logos', blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} | Manager: {self.manager}'


class FoodCategory(models.Model):
    name = models.CharField('Food Category', max_length=50)

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    name = models.CharField('Dish Name', max_length=100)
    portion_size = models.IntegerField('Portion Size')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    restaurant_dish = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.CASCADE)
    food_category = models.ForeignKey(FoodCategory, on_delete=PROTECT)

    def __str__(self):
        return f'{self.food_category} | {self.name} | {self.portion_size} gr. | {self.price} BGN'


class Menu(models.Model):
    restaurant_menu = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.CASCADE)
    menu_date = models.DateField('Menu Date', blank=True, null=True)
    dish_menu = models.ManyToManyField(Dish, blank=True)

    def __str__(self):
        return f'{self.menu_date} | {self.restaurant_menu}'
