from http import HTTPStatus
from graphene import Mutation, ObjectType, List, Field, String, ID
from graphene_django.filter import DjangoFilterConnectionField
from apps.filters import ProductFilter
from apps.models import Product, Order, OrderItem, User
from apps.types import ProductType, UserType, UserInput, ProductInput, OrderInput, OrderType, OrderItemInput, \
    OrderItemType
from graphene.types.generic import GenericScalar


class Query(ObjectType):
    all_products = DjangoFilterConnectionField(ProductType, filterset_class=ProductFilter)
    all_users = List(UserType)
    all_order_items = List(OrderItemType)

    def resolve_all_users(self, info, username=None, pk=None):
        return User.objects.all()

    def resolve_all_order_items(self, info, username=None, pk=None):
        return OrderItem.objects.all()


class CreateUser(Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = Field(UserType)

    def mutate(self, info, input):
        user = User.objects.create(**input)
        return CreateUser(user=user)


class UpdateUser(Mutation):
    class Arguments:
        id = ID(required=True)
        username = String(required=True)
        email = String(required=True)

    user = Field(UserType)

    def mutate(self, info, id, username=None, email=None):
        user = User.objects.filter(id=id)
        user.update(username=username, email=email)
        return UpdateUser(user=user.first())


class DeleteUser(Mutation):
    class Arguments:
        id = ID(required=True)

    success = String()

    def mutate(self, info, id):
        User.objects.filter(pk=id).delete()
        return DeleteUser(success=HTTPStatus.OK)


class CreateProduct(Mutation):
    class Arguments:
        input = ProductInput(required=True)

    product = Field(ProductType)

    def mutate(self, info, input):
        product = Product.objects.create(**input)
        return CreateProduct(product=product)


class CreateOrder(Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = Field(OrderType)

    def mutate(self, info, input):
        user=User.objects.filter(pk=input.user_id).first()
        order = Order.objects.create(user_id=user,amount=input.amount)
        return CreateOrder(order=order)


class DeleteOrder(Mutation):
    class Arguments:
        id = ID(required=True)

    success = GenericScalar()

    def mutate(self, info, id):
        Order.objects.filter(pk=id).delete()
        return DeleteOrder(success={'message': 'order delete', 'status': 200})


class OrderItemCreate(Mutation):
    class Arguments:
        input = OrderItemInput(required=True)

    item = Field(OrderItemType)

    def mutate(self, info, input):
        order=Order.objects.filter(pk=input.order_id).first()
        product = Product.objects.filter(pk=input.product_id).first()
        item = OrderItem.objects.create(order_id=order, product_id=product, quantity=input.quantity)
        return OrderItemCreate(item=item)


class OrderItemUpdate(Mutation):
    class Arguments:
        id = ID(required=True)
        input = OrderItemInput(required=True)

    item = Field(OrderItemType)

    def mutate(self, info, id, input):
        item = OrderItem.objects.filter(id=id)
        item.update(**input)
        return OrderItemUpdate(item=item.first())


class OrderItemDelete(Mutation):
    class Arguments:
        id = ID(required=True)

    success = GenericScalar()

    def mutate(self, info, id):
        OrderItem.objects.filter(id=id).delete()
        return OrderItemDelete(success={'message': 'order item delete', 'status': 200})
