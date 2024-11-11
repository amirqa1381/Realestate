# Generated by Django 5.1.2 on 2024-11-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_service', '0002_loanservice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='bank_account_number',
            field=models.IntegerField(max_length=12, verbose_name='Bank Account Number'),
        ),
    ]
