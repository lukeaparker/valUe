from django import forms

class CreateValueForm(forms.Form):
    value_tag = forms.CharField(max_length=15)
