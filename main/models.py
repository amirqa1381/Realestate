from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from account.models import User
from account.models import RealEstate
from django.core.exceptions import ValidationError


class Home(models.Model):
    """
    this class is for home and save the info of it
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='home')
    address = models.CharField(max_length=400, verbose_name='Address', validators=[MinLengthValidator(10)])
    meter = models.IntegerField(verbose_name='Meter')
    city = models.CharField(max_length=100, verbose_name='City')
    country = models.CharField(max_length=100, verbose_name='Country')
    postal_code = models.CharField(max_length=100, verbose_name='Postal Code')
    price = models.FloatField(verbose_name='Price')
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    description = models.TextField(verbose_name='Description')
    floor = models.PositiveIntegerField(verbose_name='Floors')
    beds = models.PositiveIntegerField(verbose_name='Beds')
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, verbose_name='RealEstate', related_name='home',
                                   null=True, blank=True)
    year_built = models.DateField(verbose_name='Year Built', default='2024-01-01')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', blank=True, null=True)

    def address_shorter(self):
        return f"{self.address[:25]}..."

    def __str__(self):
        return f"{self.owner.username}"


class Sell(models.Model):
    """
    this class is for selling, and it stores all the information of the seller and shopper
    """
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Seller',
                               related_name='sell_seller')
    shopper = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Shopper',
                                related_name='sell_shopper')
    final_price = models.FloatField(verbose_name='Final Price')
    sell_code = models.IntegerField(verbose_name='Sell Code')
    tax = models.FloatField(verbose_name='Tax', validators=[MinValueValidator(0)])
    sold_date = models.DateTimeField(auto_now_add=True, verbose_name='Sold Date')

    def clean(self):
        """
        this function is for checking that calculate tax is not lower than
        """
        if self.final_price < 0:
            raise ValidationError("The final price should not be negative")
        calculate_tax = self.final_price * 0.2
        if self.tax != calculate_tax:
            raise ValidationError(f"Tax must be {calculate_tax} based on the final price.")

    def __str__(self):
        return f"{self.final_price} -> {self.sell_code}"


class Rent(models.Model):
    """
    this class is for the rent, and we keep the information of who wants to rent the home and
    """
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='LandLord', related_name='rent_landlord')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Tenant', related_name='rent_tenant')
    final_price = models.FloatField(verbose_name='Final Price')
    rental_start_date = models.DateField(verbose_name='Rental Start Date')
    rental_end_date = models.DateField(verbose_name='Rental End Date')
    tax = models.FloatField(verbose_name='Tax', validators=[MinValueValidator(0)])

    def clean(self):
        if self.final_price < 0:
            raise ValidationError("The final price should not be negative")
        calculate_tax = self.final_price * 0.05
        if self.tax != calculate_tax:
            raise ValidationError(f"Tax must be {calculate_tax} based on the final price.")

    def __str__(self):
        return f"{self.landlord}/ {self.tenant}"


class HomeImages(models.Model):
    """
    this class is for images of the home , i made this class because it may have multiple images
    instead of one image
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name='Home', related_name='image')
    image = models.ImageField(upload_to='homes-images', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.home.owner.username
