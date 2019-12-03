from django import forms
    
class AddValueForm(forms.Form):
    value_tag = forms.CharField(help_text="Enter a value tag")