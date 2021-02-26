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

