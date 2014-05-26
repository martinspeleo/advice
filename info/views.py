from django.shortcuts import render_to_response

def home(request):
    return render_to_response("index.html")

def leaflet(request, leaflet_pk):
    return render_to_response("leaflet.html")
