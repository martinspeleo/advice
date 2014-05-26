
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

class MobileForm(forms.Form):
    mobile_number = forms.CharField()

def section_form_factory(section):
    
    properties = dict([(item.title, forms.BooleanField()) 
                       for item 
                       in section.item_set.all()])
        
    return type('SectionForm', (forms.Form,), properties)
