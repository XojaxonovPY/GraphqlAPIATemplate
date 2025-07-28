import graphene
import graphql_jwt

from apps import schema


class Query(schema.Query):
    pass


class Mutation(graphene.ObjectType):
    # ----------------- AUTH -----------------
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    # ----------------- USER -----------------
    create_user = schema.CreateUser.Field()
    update_user = schema.UpdateUser.Field()
    delete_user = schema.DeleteUser.Field()

    # ----------------- CATEGORY -----------------
    create_category = schema.CreateCategory.Field()
    update_category = schema.UpdateCategory.Field()
    delete_category = schema.DeleteCategory.Field()

    # ----------------- PRODUCT -----------------
    create_product = schema.CreateProduct.Field()

    # ----------------- DEBUG -----------------
    say_hello = schema.FormHello.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
