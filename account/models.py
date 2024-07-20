from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    this class is for making and customization od the user in the project
    """
    address = models.CharField(max_length=350, null=True, blank=True, verbose_name="Address")
    city = models.CharField(max_length=150, verbose_name="City")
    country = models.CharField(max_length=150, verbose_name="Country")
    image = models.ImageField(upload_to='user-image', null=True, blank=True, verbose_name="Image")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="Phone")

    def __str__(self):
        return self.username


class RealEstate(models.Model):
    """
    this class is for showing the real estate status and info of it
    """
    ceo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="CEO",
                            related_name='real_estate_ceo')
    address = models.CharField(max_length=350, verbose_name="Address")
    city = models.CharField(max_length=150, null=False, verbose_name="City")
    country = models.CharField(max_length=150, null=False, verbose_name="Country")
    agents = models.ManyToManyField(User, related_name='realestate', verbose_name="Agents")
    is_guarantee = models.BooleanField(default=True, verbose_name="Guarantee")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    def __str__(self):
        return f"{self.ceo.username} -> {self.city}"
