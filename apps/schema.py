from http import HTTPStatus

from django.contrib.auth.models import User
from graphene import Mutation, ObjectType, List, Schema, Field, String, ID, Boolean, Int
from graphene_django.filter import DjangoFilterConnectionField
from apps.filters import CategoryFilter, UserFilter
from apps.models import Category, Product
from apps.types import ProductType, CategoryType, UserType, UserInput, ProductInput
from graphql_jwt.decorators import login_required


class Query(ObjectType):
    all_categories = DjangoFilterConnectionField(CategoryType, filterset_class=CategoryFilter)
    all_products = List(ProductType)
    users_detail = List(UserType, id=Int())
    one_user = Field(UserType)
    all_users = DjangoFilterConnectionField(UserType, filterset_class=UserFilter)

    @login_required
    def resolve_all_categories(self, info, name, first):
        return Category.objects.all()

    @login_required
    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_users(self, info, username=None, pk=None):
        return User.objects.all()

    @login_required
    def resolve_one_user(self, info):
        user=info.context.user
        return user.profile
    def resolve_users_detail(self, info, id):
        return User.objects.filter(pk=id)


class CreateCategory(Mutation):
    class Arguments:
        name = String(required=True)

    category = Field(CategoryType)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        return CreateCategory(category=category)


class UpdateCategory(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String(required=True)

    category = Field(CategoryType)

    def mutate(self, info, id, name=None):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(Mutation):
    class Arguments:
        id = ID(required=True)

    success = Boolean()

    def mutate(self, info, id):
        category = Category.objects.filter(id=id).delete()
        return DeleteCategory(success=True)


class FormHello(Mutation):
    class Arguments:
        query = String(required=True)

    response = String()

    def mutate(self, into, query):
        if query == 'hello':
            return FormHello(response='Salom Graphql')
        else:
            return FormHello(response='Notog\'ri soz')


class CreateUser(Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = Field(UserType)

    def mutate(self, info, input):
        input.clean()
        user = User.objects.create_user(**input)
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
        category = Category.objects.get(pk=int(input.category))
        product = Product.objects.create(
            name=input.name,
            price=input.price,
            category=category,
            status=input.status.value,
            # boshqa kerakli fieldlar bo‘lsa shu yerga qo‘shing
        )
        return CreateProduct(product=product)
