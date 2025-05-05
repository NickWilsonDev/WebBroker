from django.db import models
from django.forms import ModelForm, Form
from django import forms

# Create your models here.

class Gallery(models.Model):
    description = models.CharField("Description of Photo", max_length=80, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    thumbnail = models.ImageField(null=True, blank=True)


class GalleryForm(ModelForm, Form):
    image = forms.FileField() #was ImageField
    class Meta:
        model = Gallery
        fields = ['description', 'image']
