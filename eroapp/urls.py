from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('uredjaji/', views.uredjaji),
]