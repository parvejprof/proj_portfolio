from django import forms

class ControlpanelForm(forms.Form):
    
   # user_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Username"}))
    domain_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Website"}))

    # number01 = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Numner"}))
    # number02 = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Numner"}))



from django.forms import ModelForm 
from .models import Import

# class ImportForm(ModelForm):
#   class Meta:
#    # required_css_class = 'required'
#     model = Import
#     fields = ['name','jobfile']


class ImportForm(forms.Form):
  
    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Website"}))
    upload_file = forms.FileField()



from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class GeeksForm(forms.Form): 
    name = forms.CharField() 
    geeks_field = forms.FileField()


    