from django.db import models

class Leaflet(models.Model):
    title = models.CharField(max_length=40)
    email = models.BooleanField()
    url_QR = models.BooleanField()
    long_QR = models.BooleanField()
    text = models.BooleanField()
    order = models.IntegerField()

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']

class Section(models.Model):
    leaflet = models.ForeignKey("info.Leaflet")
    title = models.CharField(max_length=40)
    unique =  models.BooleanField()
    required = models.BooleanField()
    order = models.IntegerField()

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']

class Item(models.Model):
    section = models.ForeignKey("info.Section")
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField()

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['order']

class Custom(models.Model):
    label = models.CharField(unique=True, max_length=50)
    value = models.TextField()

    def __unicode__(self):
        return unicode(self.label)

    class Meta:
        verbose_name = "Customised wording"
        verbose_name_plural = "Customised wordings"
