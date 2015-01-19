from django.db import models
from django.forms import ModelForm

# Create your models here.

"""
    This class will model the Carriers or trucking companies in the databases.
    The class Loads will eventually use this and the Customer model.
"""
class Carrier(models.Model):
    company_name = models.CharField("Companies name", max_length=30, unique=True)
    phone_number = models.CharField("Phone number", max_length=12)
    fax_number   = models.CharField("Fax number", max_length=12, blank=True)
    contact_name = models.CharField("Contact name", max_length=20, blank=True)
    email        = models.CharField("Email address", max_length=20, default='', blank=True)
    address      = models.CharField("Address", max_length=40, default='')
    fed_id       = models.CharField("Federal ID", max_length=10, default='')
    mc_id        = models.CharField("Motor carrier number", max_length=8, default='')
    number_trucks = models.CharField("Number of trucks", max_length=2, default='')

class CarrierForm(ModelForm):
    class Meta:
        model  = Carrier
        fields = ['company_name', 'phone_number', 'fax_number', 'contact_name',
                  'email', 'address', 'fed_id', 'mc_id', 'number_trucks']
