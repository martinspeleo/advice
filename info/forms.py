
from django import forms
from models import Item

class EmailForm(forms.Form):
    email = forms.EmailField(required = False)

class MobileForm(forms.Form):
    mobile_number = forms.CharField(required = False)

def clean_unique_required(self):
    cleaned_data = super(forms.Form, self).clean()
    if not max(cleaned_data.values()):
        raise forms.ValidationError("At least one of these options must be selected.")
    return cleaned_data

def selections_unique(self):
    if self.cleaned_data['choose'] is None:
        return [Item.objects.get(pk=self.cleaned_data['choose'])]
    else:
        return []

def selections_not_unique(self):
    return [Item.objects.get(pk=k.strip("i")) for k in self.cleaned_data.keys()]

def section_form_factory(section):
    if section.unique:
        if section.required:
            base_choices = []
        else:
            base_choices = [("None", "None")]
        properties = {"choose": forms.ChoiceField(
                                    choices = base_choices + 
                                              [(item.pk, item.title) 
                                               for item 
                                               in section.item_set.all()], 
                                    initial="None",
                                    widget = forms.RadioSelect(),
                                                  )
                      }
        properties["radio_buttons"] = True
        properties["selections"] = selections_unique
    else:
        properties = dict([("i%i" % item.pk, 
                            forms.BooleanField(label=item.title, 
                                               required=False)) 
                       for item 
                       in section.item_set.all()])
        if section.required:
            properties["clean"] = clean_unique_required
        properties["check_boxes"] = True
        properties["selections"] = selections_not_unique
        
    return type('SectionForm', (forms.Form,), properties)
