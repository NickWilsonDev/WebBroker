from django.db import models
from django.forms import ModelForm, Form
from django import forms
import datetime
from datetime import date

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
    email        = models.CharField("Email address", max_length=40, default='', blank=True)
    address      = models.CharField("Address", max_length=40, default='')
    fed_id       = models.CharField("Federal ID", max_length=10, default='')
    mc_id        = models.CharField("Motor carrier number", max_length=8, default='')
    number_trucks = models.CharField("Number of trucks", max_length=2, default='')

# carrier insurance related
    general_ins_date = models.DateField(help_text="Date Insurance expires", default=date.today)
    auto_ins_date = models.DateField(default=date.today)
    workerscomp_ins_date = models.DateField(default=date.today)
    workerscomp_waiver = models.BooleanField("Workers Compensation Waiver", default=False)
    cargo_ins_date = models.DateField(default=date.today)
    cargo_ins_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)

class CarrierForm(ModelForm):
    class Meta:
        model  = Carrier
        widgets = {'general_ins_date': forms.DateInput(attrs={'class': 'datepicker'}),
                   'auto_ins_date': forms.DateInput(attrs={'class': 'datepicker'}),
                   'workerscomp_ins_date': forms.DateInput(attrs={'class': 'datepicker'}),
                   'cargo_ins_date': forms.DateInput(attrs={'class': 'datepicker'})}

        fields = ['company_name', 'phone_number', 'fax_number', 'contact_name',
                  'email', 'address', 'fed_id', 'mc_id', 'number_trucks',
                  'general_ins_date', 'auto_ins_date', 'workerscomp_ins_date',
                  'workerscomp_waiver', 'cargo_ins_date', 'cargo_ins_amount']
