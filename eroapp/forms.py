from django import forms
from .models import *


"""class LokacijaForm(forms.Form):
    sifra_lokacije = forms.CharField(label="Šifra lokacije")
    mjesto = forms.CharField(label="Mjesto")
"""

class LokacijaForm(forms.ModelForm):
    class Meta:
        model = Lokacija
        fields = '__all__'
