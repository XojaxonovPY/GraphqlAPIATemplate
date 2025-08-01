from django.contrib.auth.models import User
from django_filters import FilterSet, CharFilter, NumberFilter
from apps.models import Product
from graphene import Enum


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains',field_name='name')
    max_quantity = NumberFilter(field_name='quantity', lookup_expr='gte')
    min_quantity = NumberFilter(field_name='quantity', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('name', 'quantity')





