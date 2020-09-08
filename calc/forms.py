from django import forms

class CalculateForm(forms.Form):
    number01 = forms.FloatField()
    number02 = forms.FloatField()
    user_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Username"}))

    # number01 = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Numner"}))
    # number02 = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Numner"}))

    
    