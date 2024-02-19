from django.db import models

# Create your models here.
class CommunityEntity(models.Model):
    house_number = models.CharField(max_length=100,blank=True,  null =True)
    primary_owner = models.CharField(max_length=255,blank=True,  null =True)  
    num_people = models.IntegerField(blank=True,  null =True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,  null =True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,  null =True)

 
    def __str__(self):
        return f"House {self.house_number}"