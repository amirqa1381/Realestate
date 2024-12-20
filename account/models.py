from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save



class User(AbstractUser):
    """
    this class is for making and customization od the user in the project
    """
    address = models.CharField(max_length=350, null=True, blank=True, verbose_name="Address")
    city = models.CharField(max_length=150, verbose_name="City")
    country = models.CharField(max_length=150, verbose_name="Country")
    image = models.ImageField(upload_to='user-image', null=True, blank=True, verbose_name="Image")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="Phone")
    ceo = models.BooleanField(default=False, verbose_name="CEO")

    def __str__(self):
        return self.username


class RealEstate(models.Model):
    """
    this class is for showing the real estate status and info of it
    """
    ceo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="CEO",
                            related_name='real_estate_ceo')
    Name = models.CharField(max_length=150, verbose_name="Name")
    address = models.CharField(max_length=350, verbose_name="Address")
    city = models.CharField(max_length=150, null=False, verbose_name="City")
    country = models.CharField(max_length=150, null=False, verbose_name="Country")
    is_guarantee = models.BooleanField(default=True, verbose_name="Guarantee")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    phone = models.CharField(verbose_name="Phone", max_length=11, null=True, blank=True)
    description = models.CharField(verbose_name="Description", max_length=250, null=True, blank=True)
    email = models.EmailField(verbose_name="Email", max_length=254, null=True, blank=True)

    def __str__(self):
        return self.Name


class Agent(models.Model):
    """
    this class is for the agents and every person that his/her job is agent of the houses
    should submit and register for working in the website and our service
    """
    agent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Agent', related_name='agent')
    realEstate = models.ForeignKey(RealEstate, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='RealEstate')
    joined_date = models.DateTimeField(auto_now_add=True, verbose_name="Joined date")
    working_history = models.TextField(verbose_name="Working history")
    working_year_number = models.IntegerField(verbose_name="Working year number")
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


class ProfileOfSellerOrRealEstate(models.Model):
    JOB_CHOICES = {
        'OW': 'Owner',
        'AG': 'Agent'
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='profile')
    owner_or_agent = models.CharField(choices=JOB_CHOICES, verbose_name='Owner Or Agent', max_length=10)
    job_description = models.TextField(verbose_name='Job Description')
    home_phone = models.CharField(max_length=7, verbose_name='Home Phone',
                                  validators=[MinLengthValidator(7), MaxLengthValidator(7)])
    birth_year = models.DateField(verbose_name='Birth Year')
    completed = models.BooleanField(default=False, verbose_name='Completed')

    def __str__(self):
        return self.user.username


