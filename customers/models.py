from django.db import models
from django.forms import ModelForm


# Create your models here.
class Customer(models.Model):
    company_name = models.CharField("Company name", max_length=40, unique=True)
    contact_name = models.CharField("Contact name", max_length=30)
    phone_number = models.CharField("Phone number", max_length=12)
    fax_number   = models.CharField("Fax number", max_length=12, default='', blank=True)
    address      = models.CharField("Address", max_length=40, default='')
    email_address = models.CharField("Email Address", max_length=40, default='', blank=True)

class CustomerForm(ModelForm):
    class Meta:
        model  = Customer
        fields = ['company_name', 'contact_name', 'phone_number', 'fax_number',
                  'address', 'email_address']

