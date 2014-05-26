from django.shortcuts import render
from models import *
from forms import *
from forms import section_form_factory

def home(request):
    return render(request,
                  "index.html", 
                  {"leaflets": Leaflet.objects.all()})

def leaflet(request, leaflet_pk):
    leaflet = Leaflet.objects.get(pk = leaflet_pk)
    extra_forms = []
    if request.method == 'POST':
        args = [request.POST]
    else:
        args = []
    sections = [{"title": section.title,
                 "form": section_form_factory(section)(*args, prefix=section.pk)} 
                for section 
                in leaflet.section_set.all()]
        
    if leaflet.email:
        extra_forms.append(EmailForm(*args, prefix="email"))
    if leaflet.text:
        extra_forms.append(MobileForm(*args, prefix="mobile"))
    return render(request,
                  "leaflet.html", 
                  {"leaflet": leaflet,
                   "sections": sections,
                   "extra_forms": extra_forms})
