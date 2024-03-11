from django.db import models
from django.contrib.auth.models import User, Group
from datetime import date, datetime
#from datetime import datetime
from community_units.models import CommunityEntity


class Company(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    # Add any other relevant fields as needed

    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    STATUS_CHOICES = (
        ('New/Open', 'New/Open'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review'),
        ('On Hold', 'On Hold'),
        ('Resolved/Closed', 'Resolved/Closed'),
        ('Cancelled', 'Cancelled'),
        ('Reopened', 'Reopened'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,  null =True)
    house = models.ForeignKey(CommunityEntity,on_delete=models.CASCADE, null=True,blank=True,)
    coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_opened = models.DateField(default=date.today)
    date_closed = models.DateField(blank=True,  null =True)

   # image = models.ImageField(upload_to='images/',blank=True,  null =True)
   # description = models.TextField(blank=True, null=True)
    subject = models.TextField(max_length=255,)

    Tasks =   models.CharField(max_length=20, blank=True,  null =True)
    Quotes_Invoices =   models.CharField(max_length=20, blank=True,  null =True)

    
    def __str__(self):
        return f"Work Order # {self.id}"


class Task(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Pending Parts', 'Pending Parts'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),

    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,  null =True)
    work_order = models.ForeignKey('WorkOrder', on_delete=models.SET_NULL,blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True,  null =True)
    description = models.TextField(max_length=255,)
    assigned_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    assigned_worker =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_opened = models.DateField(default=date.today)
    date_completed = models.DateField(blank=True,  null =True)
    diagnostics = models.TextField(max_length=255,)

    start_time = models.DateTimeField(blank=True,  null =True)
    end_time = models.DateTimeField(blank=True,  null =True)

    def __str__(self):
        return f"Task # {self.id}"
    


class History(models.Model):
    status = models.CharField(max_length=20,blank=True,  null =True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL,blank=True, null=True)
    image = models.ImageField(blank=True,  null =True)
    assigned_worker =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    diagnostics = models.TextField(max_length=255,blank=True, null=True)
    date = models.DateField(blank=True,  null =True)

    start_time = models.DateTimeField(blank=True,  null =True)
    end_time = models.DateTimeField(blank=True,  null =True)

    def __str__(self):
        return f"{self.date}"
    
class Quote(models.Model):
    STATUS_CHOICES = (
        ('Pending Approval', 'Pending Approval'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),

    )
    quote_number = models.CharField(max_length=50, unique=True,blank=True,  null =True) 
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    workorder = models.ForeignKey(WorkOrder, on_delete=models.SET_NULL, null=True)
   # image = models.ImageField(upload_to='quotes/',blank=True,  null =True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,  null =True)
    quote = models.FileField(upload_to='housequotes/',blank=True,  null =True)
    invoice = models.FileField(upload_to='houseinvoice/',blank=True,  null =True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    reference =  models.CharField(max_length=255, blank=True,  null =True)

    date_requested = models.DateField(default=date.today)
    date_received = models.DateField(blank=True,  null =True)
    def __str__(self):
        return f"Qoute # {self.id}"
    




