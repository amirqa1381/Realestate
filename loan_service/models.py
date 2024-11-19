from django.db import models
from account.models import User
from uuid import uuid4
from django.core.exceptions import ValidationError




class Borrower(models.Model):
    """
    this class is for the modeling the borrower who get the money if has the suitable condition
    """
    BANK = [
        ('bank_of_america','Bank Of America'),
        ('JPmorgan_chase', 'JPmorgan Chase'),
        ('td_bank', 'TD Bank'),
        ('first_citizen_bank', 'First Citizen Bank'),
        ('citibank', 'CitiBank'),
        ('wells_fargo_bank', 'Wells Fargo Bank'),
        ('pnc_bank', "PNC Bank"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="borrower", verbose_name="User")
    borrower_pid = models.UUIDField(verbose_name="Borrower_PID", unique=True, default=uuid4)
    bank_account_number = models.IntegerField(verbose_name="Bank Account Number")
    bank = models.CharField(max_length=50, verbose_name="Bank", choices=BANK, default='bank_of_america')
    is_active = models.BooleanField(verbose_name="Is Active", default=False)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    has_got_loan_service = models.BooleanField(verbose_name='has got loan service', default=False)
    activate_code = models.IntegerField(verbose_name="Activate Code", unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class LoanPrice(models.IntegerChoices):
    """
    this class is for separate the prices for choosing them
    """
    PRICE_25000 = 25000.00, '25,000.00'
    PRICE_50000 = 50000.00, '50,000.00'
    PRICE_75000 = 75000.00, '75,000.00'
    PRICE_100000 = 100000.00, '100,000.00'
    PRICE_125000 = 125000.00, '125,000.00'
    PRICE_150000 = 150000.00, '150,000.00'
    PRICE_175000 = 175000.00, '175,000.00'
    PRICE_200000 = 200000.00, '200,000.00'
    

class RefundMonth(models.IntegerChoices):
    """
    this class is for separate the months for choosing them by user
    """
    MONTH_4 = 4, '4'  
    MONTH_8 = 8, '8'  
    MONTH_12 = 12, '12'  
    


class LoanService(models.Model):
    """
    this class is for the loan service part and it handle the operation of the loan service
    """
    STATUS = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('successful', 'Successful'),
    ]
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loan_service', verbose_name='Borrower')
    price = models.FloatField(verbose_name="Price", choices=LoanPrice.choices, default=LoanPrice.PRICE_25000)
    refund_month = models.PositiveIntegerField(verbose_name="Refund Month", choices=RefundMonth.choices, default=RefundMonth.MONTH_4)
    start_time = models.DateField(verbose_name="Start time", auto_now_add=True)
    end_time = models.DateField(verbose_name="End time", null=True, blank=True)
    percentage = models.FloatField(verbose_name='Percentage', null=True, blank=True)
    total_refund = models.FloatField(verbose_name='Total Refund', null=True, blank=True)
    status = models.CharField(max_length=20 , verbose_name="Status", choices=STATUS, default="pending")
    
    def set_end_time(self):
        """
        here i want to set the end_time base on the refund month
        """
        pass
    
    def clean(self):
        super.clean()
        if self.start_time >= self.end_time:
            raise ValidationError("Start time should not be greater than or equal the End time")
    
    def calculate_percentage_and_total_fund(self):
        """
        this method is for calculating the percentage and total refund field in the model , these fields are not fill with user 
        and they are calculate base the info that user will provide to us
        """
        if self.price and self.refund_month:
            annual_interest = 0.08
            time_in_year = self.refund_month / 12
            interest = self.price * annual_interest * time_in_year
            self.total_refund = self.price + interest
            self.percentage = (interest / self.total_refund) * 100
    
    def save(self, *args, **kwargs):
        self.calculate_percentage_and_total_fund()
        return super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.borrower.user.username} -> {self.price} with {self.percentage}"
    
    