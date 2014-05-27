from django.shortcuts import render
from models import *
from forms import *
from forms import section_form_factory
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
    return render(request, 
                  "index.html", 
                  {"leaflets": Leaflet.objects.all(),
                   "custom": CUSTOM_LOOKUP})

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
    if request.method == 'POST':
        if min([form.is_valid() for form in extra_forms] +
               [section["form"].is_valid() for section in sections]):#Are all forms valid?
            
            return render(request, 
                  "confirm.html", 
                  {"custom": CUSTOM_LOOKUP}) 
    return render(request,
                  "leaflet.html", 
                  {"leaflet": leaflet,
                   "sections": sections,
                   "extra_forms": extra_forms,
                   "custom": CUSTOM_LOOKUP})

def set_up_help(request):
    return render(request, 
                  "set_up_help.html",
                  {"custom": CUSTOM_LOOKUP})
