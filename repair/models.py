from django.db import models
from main.models import Home
from account.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import random


def create_repair_code():
    """
    this function is for creating the default code for repairing the house 
    """
    random_number = random.randint(1000,10000)
    return random_number


class Mechanic(models.Model):
    """
    this class is for the mechanic model and it has store all the info of the model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mechanic', verbose_name='User')
    mechanical_engineering_code = models.CharField(verbose_name="Mechanical_code", max_length=12)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")
    is_active = models.BooleanField(verbose_name="is active", default=False)
    
    def __str__(self):
        return self.user.username

class Repair(models.Model):
    """
    this class is for keeping the house that will repair by other people
    """
    mechanic = models.ForeignKey(Mechanic, on_delete=models.SET_NULL, null=True, verbose_name='Mechanic',
                                 related_name='mechanic_repair')
    issue = models.TextField(verbose_name='Issue')
    repair_code = models.IntegerField(verbose_name='Repair Code')
    tax = models.FloatField(verbose_name='Tax', validators=[MinValueValidator(0)])
    repair_price = models.FloatField(verbose_name='Final Price', default=create_repair_code)
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True, verbose_name='Home',
                             related_name='home_repair')
    request_of_repair = models.DateField(verbose_name='Request of Repair', auto_now_add=True)
    repair_done_time = models.DateField(verbose_name='Repair Done Time', null=True, blank=True)

    def clean(self):
        if self.repair_price < 0:
            raise ValidationError("The final price should not be negative")
        repair_tax = self.repair_price * 0.02

        if self.tax != repair_tax:
            raise ValidationError(f"Tax must be {repair_tax} based on the final price.")
        

    def __str__(self):
        return f"{self.home.owner}/{self.mechanic}/{self.repair_price}"
