# Generated by Django 5.0.7 on 2024-08-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_agent_working_year_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='Name',
            field=models.CharField(default='Excellent', max_length=150, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
