# Generated by Django 5.0.7 on 2024-07-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_home_baths'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='garages',
            field=models.PositiveIntegerField(default=1, verbose_name='Garages'),
        ),
    ]
