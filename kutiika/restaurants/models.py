from django.db import models
from django.contrib.auth.models import User


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
