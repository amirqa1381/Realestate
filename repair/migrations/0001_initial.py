# Generated by Django 5.0.7 on 2024-07-26 06:01

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0008_delete_repair'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField(verbose_name='Issue')),
                ('repair_code', models.IntegerField(verbose_name='Repair Code')),
                ('tax', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tax')),
                ('repair_price', models.FloatField(verbose_name='Final Price')),
                ('request_of_repair', models.DateField(auto_now_add=True, verbose_name='Request of Repair')),
                ('repair_done_time', models.DateField(blank=True, null=True, verbose_name='Repair Done Time')),
                ('home', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_repair', to='main.home', verbose_name='Home')),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mechanic_repair', to=settings.AUTH_USER_MODEL, verbose_name='Mechanic')),
            ],
        ),
    ]