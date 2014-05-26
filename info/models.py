from django.db import models

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

class Item(models.Model):
    section = models.ForeignKey("info.Section")
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return unicode(self.title)
