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
    is_guarantee = models.BooleanField(default=True, verbose_name="Guarantee")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    def __str__(self):
        return f"{self.ceo.username} -> {self.city}"


class Agent(models.Model):
    """
    this class is for the agents and every person that his/her job is agent of the houses
    should submit and register for working in the website and our service
    """
    agent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent', related_name='agent')
    realEstate = models.ForeignKey(RealEstate, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='RealEstate')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    def __str__(self):
        return self.agent.username


class Contact(models.Model):
    """
    this class is for the contact form and keep the all the information of the contact form that user
    sent
    """
    subject = models.CharField(max_length=150, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', related_name='contact')
    created = models.DateField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name='Updated At')

    def __str__(self):
        return self.subject
