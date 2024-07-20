from django.db import models
from django.core.validators import MinLengthValidator
from account.models import User
from account.models import RealEstate


class Home(models.Model):
    """
    this class is for home and save the info of it
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='home')
    address = models.CharField(max_length=400, verbose_name='Address', validators=[MinLengthValidator(50)])
    meter = models.IntegerField(verbose_name='Meter')
    city = models.CharField(max_length=100, verbose_name='City')
    country = models.CharField(max_length=100, verbose_name='Country')
    postal_code = models.CharField(max_length=100, verbose_name='Postal Code')
    price = models.FloatField(verbose_name='Price')
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    description = models.TextField(verbose_name='Description')
    floor = models.PositiveIntegerField(verbose_name='Floors')
    beds = models.PositiveIntegerField(verbose_name='Beds')
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, verbose_name='RealEstate', related_name='home')

    def __str__(self):
        return f"{self.owner.username}"
