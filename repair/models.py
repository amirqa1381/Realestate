from django.db import models
from main.models import Home
from account.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Repair(models.Model):
    """
    this class is for keeping the house that will repair by other people
    """
    mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Mechanic',
                                 related_name='mechanic_repair')
    issue = models.TextField(verbose_name='Issue')
    repair_code = models.IntegerField(verbose_name='Repair Code')
    tax = models.FloatField(verbose_name='Tax', validators=[MinValueValidator(0)])
    repair_price = models.FloatField(verbose_name='Final Price')
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
