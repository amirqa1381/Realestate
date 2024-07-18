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
    
