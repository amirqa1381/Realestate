# Generated by Django 5.0.7 on 2024-07-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_repair'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at'),
        ),
    ]