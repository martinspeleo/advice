from django.shortcuts import render_to_response
from models import *

def home(request):
    return render_to_response("index.html", {"leaflets": Leaflet.objects.all()})

def leaflet(request, leaflet_pk):
    return render_to_response("leaflet.html", {"leaflet": Leaflet.objects.get(pk = leaflet_pk)})
