import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class LokacijaFilter(django_filters.FilterSet):
    mjesto = CharFilter(field_name='mjesto', lookup_expr='icontains')

    class Meta:
        model = Lokacija
        fields = '__all__'