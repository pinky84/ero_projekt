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

#-------------------------------------------------------------------------------------------------------

class ZgradaForm(forms.ModelForm):
    class Meta:
        model = Zgrada
        fields = '__all__'

#---------------------------------------------------------------------------------------

class ProstorijaForm(forms.ModelForm):
    class Meta:
        model = Prostorija
        fields = '__all__'

#-----------------------------------------------------------------------------------------

class KorisnikForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = '__all__'

#----------------------------------------------------------------------------------------

class UredajForm(forms.ModelForm):
    class Meta:
        model = Uredaj
        fields = '__all__'

#--------------------------------------------------------------------------------

class KvarForm(forms.ModelForm):
    class Meta:
        model = Kvar
        fields = '__all__'