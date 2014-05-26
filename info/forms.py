
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

class MobileForm(forms.Form):
    mobile_number = forms.CharField()

def section_form_factory(leaflet):
    
    properties = dict([(section.title, forms.BooleanField()) 
                       for section 
                       in self.section_set.all()])
        
    return type('SectionForm', (forms.Form,), properties)
