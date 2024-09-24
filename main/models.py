from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.text import slugify
from django.utils.timezone import now
from account.models import User
from account.models import RealEstate
from django.core.exceptions import ValidationError


class Home(models.Model):
    """
    this class is for home and save the info of it
    """
    TYPES = [
        ("RE", "Rent"),
        ("SE", "Sell")
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', related_name='home')
    address = models.CharField(max_length=400, verbose_name='Address', validators=[MinLengthValidator(10)])
    meter = models.PositiveIntegerField(verbose_name='Meter')
    city = models.CharField(max_length=100, verbose_name='City')
    country = models.CharField(max_length=100, verbose_name='Country')
    postal_code = models.CharField(max_length=100, verbose_name='Postal Code')
    price = models.FloatField(verbose_name='Price')
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    description = models.TextField(verbose_name='Description')
    floor = models.PositiveIntegerField(verbose_name='Floors')
    beds = models.PositiveIntegerField(verbose_name='Beds')
    baths = models.PositiveIntegerField(verbose_name='Bath', default=1)
    garages = models.PositiveIntegerField(verbose_name='Garages', default=1)
    realestate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, verbose_name='RealEstate', related_name='home',
                                   null=True, blank=True)
    year_built = models.DateField(verbose_name='Year Built', default=now)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', blank=True, null=True)
    slug = models.SlugField(max_length=150, verbose_name='Slug', unique=True, blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPES, default="SE")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.address_shorter())
        super(Home, self).save(*args, **kwargs)

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
    property = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name='Property', related_name='sell_property',
                                 null=True)
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
    property = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name='Property', related_name='rent_property',
                                 null=True)
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
    this class is for images of the home , I made this class because it may have multiple images
    instead of one image
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name='Home', related_name='image')
    image = models.ImageField(upload_to='homes-images', verbose_name='Image')
    alt = models.CharField(verbose_name='Alt', null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.home.owner.username


class Blog(models.Model):
    """
    this is a class that I've written for saving and showing the news of the site,
    and it'll keep the information of the news
    """
    NEWS_CATEGORY = {
        'RESIDENTIAL': 'residential',
        'COMMERCIAL': 'commercial',
        'PARK': 'park',
        'SELLING': 'selling',
        'RENTING': 'renting',
    }
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', related_name='news')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='news', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    news_category = models.CharField(max_length=15, choices=NEWS_CATEGORY, default='RESIDENTIAL')

    def __str__(self):
        return f"{self.author.username} -> {self.title}"


class PropertyRequest(models.Model):
    """
    this class is for requesting the property and keep the information of the user that send some mail
    and make connect between the different owner and bidder
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name='Home', related_name='property_request')
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email', max_length=150)
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.name
