from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from graphene import relay, InputObjectType, String, Float, ID, Decimal, Field, Argument
from graphene_django import DjangoObjectType

from apps.filters import ProductEnum
from apps.models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"
        interfaces = (relay.Node,)
        filter_fields = {
            "name": ["icontains"]
        }


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

    status = Field(ProductEnum)

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'
        interfaces = (relay.Node,)
        filter_fields = {
            'username': ['icontains','startswith'],
            'pk':['exact'],
        }


class UserInput(InputObjectType):
    username = String(required=True)
    email=String(required=True)
    password = String(required=True)

    def clean(self):
        if len(self.password) <=3:
            raise ValidationError("Password must be at least 3 characters long")

class ProductInput(InputObjectType):
    name=String(required=True)
    price=Decimal(required=True)
    category=ID(required=True)
    status = Argument(ProductEnum)
