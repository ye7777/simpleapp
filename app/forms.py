from django import forms
from .models import Name

class Nameform(forms.ModelForm):
    class Meta:
        model = Name
        fields = ["name"]