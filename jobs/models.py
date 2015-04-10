from django.db import models
from django.forms import ModelForm, Form
from django import forms


# Create your models here.

class Job(models.Model):
    job_name = models.CharField("Job Name", max_length=30, unique=True)

    COMMODITY_CHOICES = (                                                       
        ('Lime', 'Lime'), ('Sand', 'Sand'), ('Stone', 'Stone'), ('Coal', 'Coal'),
        ('Coke', 'Coke'), ('Metal', 'Metal'), ('Stainless', 'Stainless Steel'), 
        ('Feed', 'Feed Ingrediants'), ('Glass', 'Glass'), ('Produce', 'Produce'),
        ('Other', 'Other')                                                      
    )                  

    commodity = models.CharField("Commodity", max_length=17, choices=COMMODITY_CHOICES)
 
    commodity_details = models.CharField("Commodity Details", max_length=30, blank=True, null=True)

    shipper = models.CharField("Shipper", max_length=40)
    shipper_street_address = models.CharField("Street Address", max_length=40, null=True, blank=True)
    origin_city = models.CharField("Origin City", max_length=20)                
    origin_state = models.CharField("Origin State", max_length=2)               
    shipperNumber = models.CharField("Shipper Phone Number", max_length=12, null=True, blank=True)
    shipperPickupHours= models.CharField("Available Pick up Times", max_length=20, null=True, blank=True)
                                                                                
    reciever = models.CharField("Reciever", max_length=40)                      
    reciever_street_address = models.CharField("Street Address", max_length=40, null=True, blank=True)
    reciever_city = models.CharField("Destination City", max_length=20)         
    reciever_state = models.CharField("Destination State", max_length=2)        
    recieverNumber = models.CharField("Reciever Phone Number", max_length=12, null=True, blank=True)
    recieverDropOffHours= models.CharField("Available Drop off Times", max_length=20, null=True, blank=True)
                                                                                
    special_instructions = models.CharField("Special Instructions/Reference Numbers", max_length=40, blank=True, null=True)


    brokerRate = models.DecimalField(max_digits=7, decimal_places=2)            
    bfsc = models.DecimalField(max_digits=2, decimal_places=2, default=0)     
                                                                                
    carrierRate = models.DecimalField(max_digits=7, decimal_places=2)           
    cfsc = models.DecimalField(max_digits=2, decimal_places=2, default=0)     


class JobForm(ModelForm, Form):
    class Meta:
        model = Job
        fields = ['job_name', 'commodity', 'commodity_details', 'shipper',
                  'shipper_street_address', 'origin_city', 'origin_state',
                  'shipperNumber', 'shipperPickupHours', 'reciever',
                  'reciever_street_address', 'reciever_city', 'reciever_state',
                  'recieverNumber', 'recieverDropOffHours', 'special_instructions',
                  'brokerRate', 'bfsc', 'carrierRate', 'cfsc']
