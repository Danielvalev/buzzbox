from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField('Restaurant Name', max_length=120)
    address = models.CharField(max_length=300)
    description = models.CharField('Description', max_length=255)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    logo = models.ImageField(upload_to='public/restaurant_logos', blank=True, null=True)
    manager = models.CharField('Manager', max_length=50)

    def __str__(self):
        return f'{self.name} | Manager: {self.manager}'
