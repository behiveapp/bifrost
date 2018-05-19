import graphene
from lib.graphql.cart import Cart, format_cart
from lib.model.cart import Cart as CartModel
from lib.utils import normalize_field

class SellerInput(graphene.InputObjectType):
  _id = graphene.String(required=True)
  identifier = graphene.String(required=True)
  short_name = graphene.String(required=True)
  full_name = graphene.String(required=True)

class BuyerInput(graphene.InputObjectType):
  _id = graphene.String(required=True)
  identifier = graphene.String(required=True)
  name = graphene.String(required=True)

class OpenCart(graphene.Mutation):
  class Arguments:
    buyer_data = BuyerInput(required=True)
    seller_data = SellerInput(required=True)

  cart = graphene.Field(lambda: Cart)

  def mutate(self, info, buyer_data=None, seller_data=None):
    cart = CartModel.open_cart(buyer_data, seller_data)
    return OpenCart(cart=format_cart(cart))