from django.db import models
from forms import section_form_factory

class Leaflet(models.Model):
    title = models.CharField(max_length=40)
    email = models.BooleanField()
    url_QR = models.BooleanField()
    long_QR = models.BooleanField()
    text = models.BooleanField()

    def __unicode__(self):
        return unicode(self.title)

class Section(models.Model):
    leaflet = models.ForeignKey("info.Leaflet")
    title = models.CharField(max_length=40)
    unique =  models.BooleanField()
    required = models.BooleanField()

    def __unicode__(self):
        return unicode(self.title)

    def form(self):
        return section_form_factory(self)()

class Item(models.Model):
    section = models.ForeignKey("info.Section")
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return unicode(self.title)

class Custom(models.Model):
    label = models.CharField(unique=True, max_length=50)
    value = models.TextField()

    def __unicode__(self):
        return unicode(self.label)
