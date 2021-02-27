from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *

# Create your views here.

def home(request):
    return render(request, 'home.html')
"""
def uredjaji(request):
    return render(request, 'uredjaji.html')
"""

"""class LokacijaListView(ListView):
    template_name   = 'lokacija/lokacija_list_view.html'
    queryset        = Lokacija.objects.all()
    context_object_name = 'lokacije'
"""

def lokacija_list(request):
    lokacije = Lokacija.objects.all()
    context = {'lokacije': lokacije}
    return render(request, 'lokacija/lokacija_list_view.html', context)

def lokacija_detail(request, pk):
    lokacija = Lokacija.objects.get(id=pk)
    context = {'lokacija': lokacija}
    return render(request, 'lokacija/lokacija_detail.html', context)

def lokacija_create(request):
    form = LokacijaForm()
    if request.method == "POST":
        form = LokacijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/lokacije")
    context = {'form': form}
    return render(request, 'lokacija/lokacija_create.html', context)

def lokacija_update(request, pk):
    lokacija = Lokacija.objects.get(id=pk)
    form = LokacijaForm(instance=lokacija)
    if request.method == "POST":
        form = LokacijaForm(request.POST, instance=lokacija)
        if form.is_valid():
            form.save()
            return redirect("/lokacije")
    context = {
        'form': form,
        'lokacija': lokacija
        }
    return render(request, 'lokacija/lokacija_update.html', context)

def lokacija_delete(request, pk):
    lokacija = Lokacija.objects.get(id=pk)
    lokacija.delete()
    return redirect("/lokacije")
#------------------------------------------------------------------------------------------------

def zgrada_list(request):
    zgrade = Zgrada.objects.all()
    context = {'zgrade': zgrade}
    return render(request, 'zgrada/zgrada_list.html', context)

def zgrada_detail(request, pk):
    zgrada = Zgrada.objects.get(id=pk)
    context = {'zgrada': zgrada}
    return render(request, 'zgrada/zgrada_detail.html', context)

def zgrada_create(request):
    form = ZgradaForm()
    if request.method == "POST":
        form = ZgradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/zgrade")
    context = {'form': form}
    return render(request, 'zgrada/zgrada_create.html', context)

def zgrada_update(request, pk):
    zgrada = Zgrada.objects.get(id=pk)
    form = ZgradaForm(instance=zgrada)
    if request.method == "POST":
        form = ZgradaForm(request.POST, instance=zgrada)
        if form.is_valid():
            form.save()
            return redirect("/zgrade")
    context = {
        'form': form,
        'zgrada': zgrada
        }
    return render(request, 'zgrada/zgrada_update.html', context)

def zgrada_delete(request, pk):
    zgrada = Zgrada.objects.get(id=pk)
    zgrada.delete()
    return redirect("/zgrade")

#----------------------------------------------------------------------------------------------

def prostorija_list(request):
    prostorije = Prostorija.objects.all()
    context = {'prostorije': prostorije}
    return render(request, 'prostorija/prostorija_list.html', context)

def prostorija_detail(request, pk):
    prostorija = Prostorija.objects.get(id=pk)
    context = {'prostorija': prostorija}
    return render(request, 'prostorija/prostorija_detail.html', context)

def prostorija_create(request):
    form = ProstorijaForm()
    if request.method == "POST":
        form = ProstorijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/prostorije")
    context = {'form': form}
    return render(request, 'prostorija/prostorija_create.html', context)

def prostorija_update(request, pk):
    prostorija = Prostorija.objects.get(id=pk)
    form = ProstorijaForm(instance=prostorija)
    if request.method == "POST":
        form = ProstorijaForm(request.POST, instance=prostorija)
        if form.is_valid():
            form.save()
            return redirect("/prostorije")
    context = {
        'form': form,
        'prostorija': prostorija
        }
    return render(request, 'prostorija/prostorija_update.html', context)

def prostorija_delete(request, pk):
    prostorija = Prostorija.objects.get(id=pk)
    prostorija.delete()
    return redirect("/prostorije")

#---------------------------------------------------------------------------------------------

def korisnik_list(request):
    korisnici = Korisnik.objects.all()
    context = {'korisnici': korisnici}
    return render(request, 'korisnik/korisnik_list.html', context)

def korisnik_detail(request, pk):
    korisnik = Korisnik.objects.get(id=pk)
    context = {'korisnik': korisnik}
    return render(request, 'korisnik/korisnik_detail.html', context)

def korisnik_create(request):
    form = KorisnikForm()
    if request.method == "POST":
        form = KorisnikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/korisnici")
    context = {'form': form}
    return render(request, 'korisnik/korisnik_create.html', context)

def korisnik_update(request, pk):
    korisnik = Korisnik.objects.get(id=pk)
    form = KorisnikForm(instance=korisnik)
    if request.method == "POST":
        form = KorisnikForm(request.POST, instance=korisnik)
        if form.is_valid():
            form.save()
            return redirect("/korisnici")
    context = {
        'form': form,
        'korisnik': korisnik
        }
    return render(request, 'korisnik/korisnik_update.html', context)

def korisnik_delete(request, pk):
    korisnik = Korisnik.objects.get(id=pk)
    korisnik.delete()
    return redirect("/korisnici")

#------------------------------------------------------------------------------------------

def uredaj_list(request):
    uredaji = Uredaj.objects.all()
    context = {'uredaji': uredaji}
    return render(request, 'uredaj/uredaj_list.html', context)

def uredaj_detail(request, pk):
    uredaj = Uredaj.objects.get(id=pk)
    context = {'uredaj': uredaj}
    return render(request, 'uredaj/uredaj_detail.html', context)

def uredaj_create(request):
    form = UredajForm()
    if request.method == "POST":
        form = UredajForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/uredaji")
    context = {'form': form}
    return render(request, 'uredaj/uredaj_create.html', context)

def uredaj_update(request, pk):
    uredaj = Uredaj.objects.get(id=pk)
    form = UredajForm(instance=uredaj)
    if request.method == "POST":
        form = UredajForm(request.POST, instance=uredaj)
        if form.is_valid():
            form.save()
            return redirect("/uredaji")
    context = {
        'form': form,
        'korisnik': uredaj
        }
    return render(request, 'uredaj/uredaj_update.html', context)

def uredaj_delete(request, pk):
    uredaj = Uredaj.objects.get(id=pk)
    uredaj.delete()
    return redirect("/uredaji")

#-----------------------------------------------------------------------------------------------



