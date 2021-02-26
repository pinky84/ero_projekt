from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home),
    path('lokacije/', views.lokacija_list),
    path('lokacije/create/', views.lokacija_create),
    path('lokacije/<int:pk>/', views.lokacija_detail),

    #path('lokacije/', LokacijaListView.as_view(), name='lokacija_list_view'),
]