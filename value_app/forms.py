from django import forms

class CreateValueForm(forms.ModelForm):
    value_tag = forms.CharField(max_length=15)
   