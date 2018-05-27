import graphene
from lib.graphql.cart import Cart, format_cart
from lib.model.cart import Cart as CartModel
from lib.utils import normalize_field

class CloseCart(graphene.Mutation):
  class Arguments:
    cart_id = graphene.String(required=True)

  cart = graphene.Field(lambda: Cart)

  def mutate(self, info, cart_id=None):
    cart = CartModel.close_cart(cart_id)
    return CloseCart(cart=format_cart(cart))