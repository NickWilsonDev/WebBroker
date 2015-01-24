from django.db import models
from django.forms import ModelForm, ChoiceField, Form
from django.core.exceptions import ValidationError
from django.core import validators

from django import forms

import datetime

from customers.models import Customer
from carriers.models import Carrier
# Create your models here.


class Load(models.Model):
    COMMODITY_CHOICES = (
        ('Lime', 'Lime'), ('Sand', 'Sand'), ('Stone', 'Stone'), ('Coal', 'Coal'), 
        ('Coke', 'Coke'), ('Metal', 'Metal'), ('Stainless', 'Stainless Steel'), 
        ('Feed', 'Feed Ingrediants'), ('Glass', 'Glass'), ('Produce', 'Produce'),
        ('Other', 'Other')
    )

    commodity = models.CharField("Commodity", max_length=17, choices=COMMODITY_CHOICES)
    commodity_details = models.CharField("Commodity Details", max_length=30, blank=True, null=True)
    
    shipper = models.CharField("Shipper", max_length=40)
    origin_city = models.CharField("Origin City", max_length=20)
    origin_state = models.CharField("Origin State", max_length=2)
    shipperNumber = models.CharField("Shipper Phone Number", max_length=12, null=True, blank=True)
    shipperPickupHours= models.CharField("Available Pick up Times", max_length=20, null=True, blank=True)
        
    reciever = models.CharField("Reciever", max_length=40)
    reciever_city = models.CharField("Destination City", max_length=20)
    reciever_state = models.CharField("Destination State", max_length=2)
    recieverNumber = models.CharField("Reciever Phone Number", max_length=12, null=True, blank=True)
    recieverDropOffHours= models.CharField("Available Drop off Times", max_length=20, null=True, blank=True)
   
    special_instructions = models.CharField("Special Instructions/Reference Numbers", max_length=40, blank=True, null=True)

    customer = models.CharField("Customer", max_length=40, default="")

    carrier = models.CharField("Carrier", max_length=40, default="")

    date = models.DateField(blank=False, help_text="Date load will appear in application")
    pickupDate = models.DateField(blank=False)
    recieveDate = models.DateField(blank=False)
#########

    brokerRate = models.DecimalField(max_digits=7, decimal_places=2)
    brokerPercent = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)
    bfsc = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)

    carrierRate = models.DecimalField(max_digits=7, decimal_places=2)
    carrierPercent = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)
    cfsc = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)

    loadConfirmed = models.BooleanField("Confirmed", default=False)

# NOT DONE NEED MORE FIELDS AND MAKE A FORM


class LoadForm(ModelForm, Form):

    def __init__(self, *args, **kwargs):
        super(LoadForm, self).__init__(*args, **kwargs)
        CUSTOMER_CHOICES = Customer.objects.all()
        custList = []
        for customer in CUSTOMER_CHOICES:
            tempTuple = [(customer.company_name), (customer.company_name)]
            custList.append(tempTuple)

        CARRIER_CHOICES = Carrier.objects.all()
        carrList = []
        for carrier in CARRIER_CHOICES:
            tempTuple = [(carrier.company_name), (carrier.company_name)]
            carrList.append(tempTuple)

        self.fields['customer'] = forms.CharField(widget=forms.Select(choices=custList))
        self.fields['carrier'] = forms.CharField(widget=forms.Select(choices=carrList))

    class Meta:
        model = Load
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'}),
                   'pickupDate': forms.DateInput(attrs={'class': 'datepicker'}),
                   'recieveDate': forms.DateInput(attrs={'class': 'datepicker'})}

        fields = ['date', 'customer', 'carrier', 'commodity', 'commodity_details', 
                  'shipper', 'origin_city', 'origin_state', 'shipperNumber',
                  'shipperPickupHours', 'reciever', 'reciever_city', 
                  'reciever_state', 'recieverNumber', 'recieverDropOffHours', 
                  'special_instructions', 'brokerRate', 'brokerPercent', 'bfsc', 'carrierRate', 
                  'carrierPercent', 'cfsc', 'pickupDate', 'recieveDate', 
                  'loadConfirmed']
    
