# Generated by Django 3.2.9 on 2021-12-09 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_dish_foodcategory_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='dish_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.dish'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_date',
            field=models.DateField(blank=True, null=True, verbose_name='Menu Date'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant'),
        ),
    ]
