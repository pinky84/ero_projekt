from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home),
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

    #path('lokacije/', LokacijaListView.as_view(), name='lokacija_list_view'),
]