from django.shortcuts import render
from models import *
from forms import *
from forms import section_form_factory
from default_values import defaults, descriptions
import itertools

class CustomLookup:
    def __getitem__(self, label):
        try:
            return Custom.objects.get(label=label).value
        except Custom.DoesNotExist:
            return lookup(label)

def lookup(label):
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
        #Are all forms valid?
        if min([form.is_valid() for form in extra_forms] +
               [section["form"].is_valid() for section in sections] + 
               [True]): # final True item to handle case when there are no forms.
            selected_items = itertools.chain(*[section["form"].selections() for section in sections])
            return render(request, 
                  "confirm.html", 
                  {"leaflet": leaflet,
                   "selected_items": selected_items,
                   "custom": CUSTOM_LOOKUP}) 
    return render(request,
                  "leaflet.html", 
                  {"leaflet": leaflet,
                   "sections": sections,
                   "extra_forms": extra_forms,
                   "custom": CUSTOM_LOOKUP})


def set_up_help(request):
    custom_help = [{"label": label, "default": lookup(label), "description": description} 
                   for label, description 
                   in descriptions.items()]
    return render(request, 
                  "set_up_help.html",
                  {"custom": CUSTOM_LOOKUP, "custom_help": custom_help})
