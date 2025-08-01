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
    # ----------------- PRODUCT -----------------
    create_product = schema.CreateProduct.Field()
    # ----------------- ORDER -----------------
    create_order = schema.CreateOrder.Field()
    delete_order = schema.DeleteOrder.Field()
    # ----------------- ORDER ITEM  -----------------
    create_order_item = schema.OrderItemCreate.Field()
    update_order_item = schema.OrderItemUpdate.Field()
    delete_order_item = schema.OrderItemDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
