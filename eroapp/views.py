from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout

from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .filters import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def skocni(request):
    return render(request, 'skocni.html')
#--------------------------------------------------------------------------------------------
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/uredaji')
       # else:
           # messages.info(request, 'Pogrešno korisnički ime ili lozinka')

    context = {}
    return render(request, 'login.html', context)
#--------------------------------------------------------------------------------------------

def logout_user(request):
    logout(request)
    return redirect("/login")
#---------------------------------------------------------------------------------------
"""
def uredjaji(request):
    return render(request, 'uredjaji.html')
"""

"""class LokacijaListView(ListView):
    template_name   = 'lokacija/lokacija_list_view.html'
    queryset        = Lokacija.objects.all()
    context_object_name = 'lokacije'
"""
@login_required(login_url='/login')
def lokacija_list(request):
    lokacije = Lokacija.objects.all()

    #lokacije_set = lokacija_list.lokacija_set.all()

    my_filter = LokacijaFilter(request.GET, queryset=lokacije)  #filter
    lokacije = my_filter.qs

    context = {'lokacije': lokacije, 'my_filter': my_filter}
    return render(request, 'lokacija/lokacija_list_view.html', context)

@login_required(login_url='/login')
def lokacija_detail(request, pk):
    lokacija = Lokacija.objects.get(id=pk)
    context = {'lokacija': lokacija}
    return render(request, 'lokacija/lokacija_detail.html', context)

@login_required(login_url='/login')
def lokacija_create(request):
    form = LokacijaForm()
    if request.method == "POST":
        form = LokacijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/lokacije")
    context = {'form': form}
    return render(request, 'lokacija/lokacija_create.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def zgrada_list(request):
    zgrade = Zgrada.objects.all()
    context = {'zgrade': zgrade}
    return render(request, 'zgrada/zgrada_list.html', context)

@login_required(login_url='/login')
def zgrada_detail(request, pk):
    zgrada = Zgrada.objects.get(id=pk)
    context = {'zgrada': zgrada}
    return render(request, 'zgrada/zgrada_detail.html', context)

@login_required(login_url='/login')
def zgrada_create(request):
    form = ZgradaForm()
    if request.method == "POST":
        form = ZgradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/zgrade")
    context = {'form': form}
    return render(request, 'zgrada/zgrada_create.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def prostorija_list(request):
    prostorije = Prostorija.objects.all()
    context = {'prostorije': prostorije}
    return render(request, 'prostorija/prostorija_list.html', context)

@login_required(login_url='/login')
def prostorija_detail(request, pk):
    prostorija = Prostorija.objects.get(id=pk)
    context = {'prostorija': prostorija}
    return render(request, 'prostorija/prostorija_detail.html', context)

@login_required(login_url='/login')
def prostorija_create(request):
    form = ProstorijaForm()
    if request.method == "POST":
        form = ProstorijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/prostorije")
    context = {'form': form}
    return render(request, 'prostorija/prostorija_create.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def korisnik_list(request):
    korisnici = Korisnik.objects.all()
    context = {'korisnici': korisnici}
    return render(request, 'korisnik/korisnik_list.html', context)

@login_required(login_url='/login')
def korisnik_detail(request, pk):
    korisnik = Korisnik.objects.get(id=pk)
    context = {'korisnik': korisnik}
    return render(request, 'korisnik/korisnik_detail.html', context)

@login_required(login_url='/login')
def korisnik_create(request):
    form = KorisnikForm()
    if request.method == "POST":
        form = KorisnikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/korisnici")
    context = {'form': form}
    return render(request, 'korisnik/korisnik_create.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def uredaj_list(request):
    uredaji = Uredaj.objects.all()
    context = {'uredaji': uredaji}
    return render(request, 'uredaj/uredaj_list.html', context)

@login_required(login_url='/login')
def uredaj_detail(request, pk):
    uredaj = Uredaj.objects.get(id=pk)
    context = {'uredaj': uredaj}
    return render(request, 'uredaj/uredaj_detail.html', context)

@login_required(login_url='/login')
def uredaj_create(request):
    form = UredajForm()
    if request.method == "POST":
        form = UredajForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/uredaji")
    context = {'form': form}
    return render(request, 'uredaj/uredaj_create.html', context)

@login_required(login_url='/login')
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
        'uredaj': uredaj
        }
    return render(request, 'uredaj/uredaj_update.html', context)

def uredaj_delete(request, pk):
    uredaj = Uredaj.objects.get(id=pk)
    uredaj.delete()
    return redirect("/uredaji")

#-----------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def kvar_list(request):
    kvarovi = Kvar.objects.all()
    context = {'kvarovi': kvarovi}
    return render(request, 'kvar/kvar_list.html', context)

@login_required(login_url='/login')
def kvar_detail(request, pk):
    kvar = Kvar.objects.get(id=pk)
    context = {'kvar': kvar}
    return render(request, 'kvar/kvar_detail.html', context)

@login_required(login_url='/login')
def kvar_create(request):
    form = KvarForm()
    if request.method == "POST":
        form = KvarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/kvarovi")
    context = {'form': form}
    return render(request, 'kvar/kvar_create.html', context)

@login_required(login_url='/login')
def kvar_update(request, pk):
    kvar = Kvar.objects.get(id=pk)
    form = KvarForm(instance=kvar)
    if request.method == "POST":
        form = KvarForm(request.POST, instance=kvar)
        if form.is_valid():
            form.save()
            return redirect("/kvarovi")
    context = {
        'form': form,
        'kvar': kvar
        }
    return render(request, 'kvar/kvar_update.html', context)

def kvar_delete(request, pk):
    kvar = Kvar.objects.get(id=pk)
    kvar.delete()
    return redirect("/kvarovi")

"""def confirm_delete(request, pk):
    kvar = Kvar.objects.get(id=pk)
    context = {'kvar': kvar}
    return render(request, 'kvar/kvar_delete.html', context)
"""

