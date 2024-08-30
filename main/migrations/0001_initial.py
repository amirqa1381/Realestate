# Generated by Django 5.0.7 on 2024-08-30 09:42

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='news', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('news_category', models.CharField(choices=[('RESIDENTIAL', 'residential'), ('COMMERCIAL', 'commercial'), ('PARK', 'park'), ('SELLING', 'selling'), ('RENTING', 'renting')], default='RESIDENTIAL', max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Address')),
                ('meter', models.PositiveIntegerField(verbose_name='Meter')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('postal_code', models.CharField(max_length=100, verbose_name='Postal Code')),
                ('price', models.FloatField(verbose_name='Price')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('description', models.TextField(verbose_name='Description')),
                ('floor', models.PositiveIntegerField(verbose_name='Floors')),
                ('beds', models.PositiveIntegerField(verbose_name='Beds')),
                ('baths', models.PositiveIntegerField(default=1, verbose_name='Bath')),
                ('garages', models.PositiveIntegerField(default=1, verbose_name='Garages')),
                ('year_built', models.DateField(default=django.utils.timezone.now, verbose_name='Year Built')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='Slug')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('realestate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='account.realestate', verbose_name='RealEstate')),
            ],
        ),
        migrations.CreateModel(
            name='HomeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='homes-images', verbose_name='Image')),
                ('alt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alt')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='main.home', verbose_name='Home')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_request', to='main.home', verbose_name='Home')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.FloatField(verbose_name='Final Price')),
                ('rental_start_date', models.DateField(verbose_name='Rental Start Date')),
                ('rental_end_date', models.DateField(verbose_name='Rental End Date')),
                ('tax', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tax')),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_landlord', to=settings.AUTH_USER_MODEL, verbose_name='LandLord')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rent_property', to='main.home', verbose_name='Property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_tenant', to=settings.AUTH_USER_MODEL, verbose_name='Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.FloatField(verbose_name='Final Price')),
                ('sell_code', models.IntegerField(verbose_name='Sell Code')),
                ('tax', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tax')),
                ('sold_date', models.DateTimeField(auto_now_add=True, verbose_name='Sold Date')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell_property', to='main.home', verbose_name='Property')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sell_seller', to=settings.AUTH_USER_MODEL, verbose_name='Seller')),
                ('shopper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sell_shopper', to=settings.AUTH_USER_MODEL, verbose_name='Shopper')),
            ],
        ),
    ]
