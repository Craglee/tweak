from pyexpat import model
from unicodedata import name
from django.db import models
from django.urls import reverse
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)

class Inquiry(models.Model):
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    number = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)