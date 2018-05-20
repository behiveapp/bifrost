import graphene
from lib.graphql.cart import Cart, format_cart
from lib.model.cart import Cart as CartModel
from lib.utils import normalize_field

class AddProduct(graphene.Mutation):
  class Arguments:
    cart_id = graphene.String(required=True)
    product_id = graphene.String(required=True)

  cart = graphene.Field(lambda: Cart)

  def mutate(self, info, cart_id=None, product_id=None):
    cart = CartModel.add_product(cart_id, product_id)
    return AddProduct(cart=format_cart(cart))