from django import forms
from value_app.models import Value  

class CreateValueForm(forms.ModelForm):
    model = Value
    class Meta:
        model = Value
        fields = ['tag']
