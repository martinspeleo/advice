from django.db import models

class Leaflet(models.Model):
    title = models.CharField(max_length=40)
    email = models.BooleanField()
    url_QR = models.BooleanField()
    long_QR = models.BooleanField()
    text = models.BooleanField()

class Section(models.Model):
    title = models.CharField(max_length=40)
    unique =  models.BooleanField()
    required = models.BooleanField()

class Item(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
