from django.shortcuts import render_to_response
from models import *
from forms import *
from default_values import defaults

class CustomLookup:
    def __getitem__(self, label):
        try:
            return Custom.objects.get(label=label).value
        except Custom.DoesNotExist:
            try:
                return defaults[label]
            except KeyError:
                 return defaults[None]

CUSTOM_LOOKUP = CustomLookup()

def home(request):
    return render_to_response("index.html", 
                              {"leaflets": Leaflet.objects.all(),
                               "custom": CUSTOM_LOOKUP})

def leaflet(request, leaflet_pk):
    leaflet = Leaflet.objects.get(pk = leaflet_pk)
    extra_forms = []
    if leaflet.email:
        extra_forms.append(EmailForm)
    if leaflet.text:
        extra_forms.append(MobileForm)
    return render_to_response("leaflet.html", 
                              {"leaflet": leaflet,
                               "extra_forms": extra_forms})
