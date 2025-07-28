from django.contrib.auth.models import User
from django_filters import FilterSet, CharFilter, NumberFilter
from apps.models import Category, Product
from graphene import Enum

class CategoryFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ('name',)


class UserFilter(FilterSet):
    pk = NumberFilter(lookup_expr='icontains')
    username = CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ('username', 'pk')




class ProductEnum(Enum):
    NEW = Product.ProductStatus.NEW.value
    OLD = Product.ProductStatus.OLD.value


