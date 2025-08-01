
from graphene import relay, InputObjectType, String, Decimal, Field, Argument, Int
from graphene_django import DjangoObjectType
from apps.models import Product, Order, OrderItem,User


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"
        interfaces = (relay.Node,)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
        fields = '__all__'


class UserInput(InputObjectType):
    first_name = String()
    last_name = String()
    username = String()
    age = Int()
    phone_number = String()


class ProductInput(InputObjectType):
    name = String()
    quantity = Int()
    price = Decimal()
    image = String()


class OrderInput(InputObjectType):
    user_id = Int()
    amount = Decimal()


class OrderItemInput(InputObjectType):
    product_id = Int()
    quantity = Int()
    order_id = Int()
