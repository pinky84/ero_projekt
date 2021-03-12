from django import forms
from django.contrib.auth.models import User
from .models import *


"""class LokacijaForm(forms.Form):
    sifra_lokacije = forms.CharField(label="Šifra lokacije")
    mjesto = forms.CharField(label="Mjesto")
"""

class DateInput(forms.DateInput):   # za date widget
    input_type = 'date'

#---------------------------------------------------------------------------------

class LokacijaForm(forms.ModelForm):
    class Meta:
        model = Lokacija
        fields = '__all__'

        widgets = {
            'sifra_lokacije': forms.TextInput(attrs={'class': 'form-control'}),
            'mjesto': forms.TextInput(attrs={'class': 'form-control'}),
        }

#-------------------------------------------------------------------------------------------------------

class ZgradaForm(forms.ModelForm):
    class Meta:
        model = Zgrada
        fields = '__all__'

        widgets = {
            'sifra_zgrade': forms.TextInput(attrs={'class': 'form-control'}),
            'adresa': forms.TextInput(attrs={'class': 'form-control'}),
            'subnet': forms.TextInput(attrs={'class': 'form-control'}),
            'id_lokacija': forms.Select(attrs={'class': 'form-control'}),
        }

#---------------------------------------------------------------------------------------

class ProstorijaForm(forms.ModelForm):
    class Meta:
        model = Prostorija
        fields = '__all__'

        widgets = {
            'sifra_prostorije': forms.TextInput(attrs={'class': 'form-control'}),
            'kat': forms.TextInput(attrs={'class': 'form-control'}),
            'broj_prostorije': forms.TextInput(attrs={'class': 'form-control'}),
            'id_zgrada': forms.Select(attrs={'class': 'form-control'}),
        }

#-----------------------------------------------------------------------------------------

class KorisnikForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = '__all__'

        widgets = {
            'id_korisnika': forms.TextInput(attrs={'class': 'form-control'}),
            'ime': forms.TextInput(attrs={'class': 'form-control'}),
            'prezime': forms.TextInput(attrs={'class': 'form-control'}),
        }

#----------------------------------------------------------------------------------------

class UredajForm(forms.ModelForm):
    class Meta:
        model = Uredaj
        fields = '__all__'
        widgets = {
            'datum_nabave': DateInput(),
            'datum_isteka_garancije': DateInput(),
            'barcode': forms.TextInput(attrs={'class': 'form-control'}),
            'serijski_broj': forms.TextInput(attrs={'class': 'form-control'}),
            'vrsta_uredaja': forms.Select(attrs={'class': 'form-control'}),
            'proizvodac': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'mac_adresa': forms.TextInput(attrs={'class': 'form-control'}),
            'opis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'napomena': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'id_prostorija': forms.Select(attrs={'class': 'form-control'}),
            'korisnik_id': forms.Select(attrs={'class': 'form-control'}),
        }

#--------------------------------------------------------------------------------

class KvarForm(forms.ModelForm):
    class Meta:
        model = Kvar
        fields = '__all__'

        widgets = {
            'id_kvara': forms.TextInput(attrs={'class': 'form-control'}),
            'opis_kvara': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'barcode_uredaja': forms.Select(attrs={'class': 'form-control'}),
        }