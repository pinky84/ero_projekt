from django.urls import path
from . import views
from .views import *


urlpatterns = [
    #path('', views.home),
    path('skocni/', views.skocni),
    path('', views.login_page),
    path('login/', views.login_page),
    path('logout/', views.logout_user),
#-----------------------------------------------------------------------------
    path('lokacije/', views.lokacija_list),
    path('lokacije/<int:pk>/', views.lokacija_detail),
    path('lokacije/<int:pk>/update/', views.lokacija_update),
    path('lokacije/<int:pk>/delete/', views.lokacija_delete),
    path('lokacije/create/', views.lokacija_create),
#------------------------------------------------------------------------------
    path('zgrade/', views.zgrada_list),
    path('zgrade/<int:pk>/', views.zgrada_detail),
    path('zgrade/create/', views.zgrada_create),
    path('zgrade/<int:pk>/update/', views.zgrada_update),
    path('zgrade/<int:pk>/delete/', views.zgrada_delete),
#------------------------------------------------------------------------------
    path('prostorije/', views.prostorija_list),
    path('prostorije/<int:pk>/', views.prostorija_detail),
    path('prostorije/<int:pk>/update/', views.prostorija_update),
    path('prostorije/<int:pk>/delete/', views.prostorija_delete),
    path('prostorije/create/', views.prostorija_create),
#------------------------------------------------------------------------------
    path('korisnici/', views.korisnik_list),
    path('korisnici/<int:pk>/', views.korisnik_detail),
    path('korisnici/create/', views.korisnik_create),
    path('korisnici/<int:pk>/update/', views.korisnik_update),
    path('korisnici/<int:pk>/delete/', views.korisnik_delete),
#------------------------------------------------------------------------------
    path('uredaji/', views.uredaj_list),
    path('uredaji/<int:pk>/', views.uredaj_detail),
    path('uredaji/create/', views.uredaj_create),
    path('uredaji/<int:pk>/update/', views.uredaj_update),
    path('uredaji/<int:pk>/delete/', views.uredaj_delete),
#------------------------------------------------------------------------------
    path('kvarovi/', views.kvar_list),
    path('kvarovi/<int:pk>/', views.kvar_detail),
    path('kvarovi/create/', views.kvar_create),
    path('kvarovi/<int:pk>/update/', views.kvar_update),
   # path('kvarovi/<int:pk>/confirm_delete/', views.confirm_delete),
    path('kvarovi/<int:pk>/delete/', views.kvar_delete),

    #path('lokacije/', LokacijaListView.as_view(), name='lokacija_list_view'),
]