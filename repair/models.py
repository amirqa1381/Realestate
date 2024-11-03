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
    issue = models.TextField(verbose_name='Issue')
    repair_code = models.IntegerField(verbose_name='Repair Code',default=create_repair_code)
    tax = models.FloatField(verbose_name='Tax', validators=[MinValueValidator(0)], null=True, blank=True)
    repair_price = models.FloatField(verbose_name='Final Price', null=True, blank=True)
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True, verbose_name='Home',
                             related_name='home_repair')
    request_of_repair = models.DateField(verbose_name='Request of Repair', auto_now_add=True)
    repair_done_time = models.DateField(verbose_name='Repair Done Time', null=True, blank=True)

    def clean(self):
        if self.repair_price is not None and int(self.repair_price) < 0:
            raise ValidationError("The final price should not be negative")
        
        if self.repair_price is not None:
            repair_tax = self.repair_price * 0.03
            if self.tax != repair_tax:
                raise ValidationError(f"Tax must be {repair_tax} based on the final price.")
            
            
    def save(self, *args, **kwargs):
        # here we check the meter of the home that user send the repair request for it
        if self.home:
            if self.home.meter < 100:
                self.repair_price = 25
            elif 100 <= self.home.meter < 250:
                self.repair_price = 75
            else:
                self.repair_price = 100
            
            self.tax = self.repair_price * 0.03
        return super().save(*args, **kwargs) # Call the parent class of the save method
            

    def __str__(self):
        return f"{self.home.owner}/{self.mechanic}/{self.repair_price}"





class RepairImages(models.Model):
    """
    here is the class that is for the images that user will submit for the problem that the home has 
    """
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, verbose_name='Repair Images', related_name='home_images_problem')
    alt = models.CharField(max_length=250, verbose_name='Alt')
    images = models.ImageField(upload_to="RepairImages", verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    def __str__(self):
        return str(self.repair.home.address)
    
    

class MechanicRequestForRepair(models.Model):
    """
    this class is for the request of the mechanic and we handle the requests with this model
    """
    STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE,related_name="mechanic_request", verbose_name="mechanic")
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE,related_name="repair_mechanic_request", verbose_name="repair")
    request_send_time = models.DateTimeField(auto_now_add=True, verbose_name="Request Send Time")
    start_time = models.DateTimeField(verbose_name="Start time")
    end_time = models.DateTimeField(verbose_name="End time")
    repair_duration = models.DurationField(null=True, blank=True, verbose_name="Repair duration")
    status = models.CharField(verbose_name="Status", choices=STATUS, default='pending', max_length=20)
    
    
    def save(self, *args, **kwargs):
        # here we check that the start time and the end time are represented for our project
        if self.start_time and self.end_time:
            self.repair_duration = self.end_time - self.start_time
        else:
            self.repair_duration = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Request by {self.mechanic} - Status: {self.status}" 
    