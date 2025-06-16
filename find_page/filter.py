import django_filters
from .models import MySpisok

class MySpisokFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Поиск по имени

    class Meta:
        model = MySpisok
        fields = ['name', 'year_create', 'kp_rate']