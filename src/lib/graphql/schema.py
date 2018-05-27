import graphene
from lib.graphql.product import Product, resolve_Products
from lib.graphql.seller import Seller, resolve_Sellers
from lib.graphql.buyer import Buyer, resolve_Buyers
from lib.graphql.cart import Cart as CartSchema, resolve_Cart, resolve_Carts
from lib.graphql.mutations.open_cart import OpenCart
from lib.graphql.mutations.add_product import AddProduct
from lib.graphql.mutations.close_cart import CloseCart

class Query(graphene.ObjectType):
  Sellers = graphene.Field(graphene.List(lambda: Seller), name=graphene.String())
  Products = graphene.Field(graphene.List(lambda: Product), name=graphene.String(), category=graphene.String(), sellerIdentifier=graphene.String())
  Buyers = graphene.Field(graphene.List(lambda: Buyer))
  Cart = graphene.Field(CartSchema, id=graphene.String())
  Carts = graphene.Field(graphene.List(lambda: CartSchema), sellerId=graphene.String(), buyerId=graphene.String(), status=graphene.Int())

  def resolve_Sellers(self, info, name):
    return resolve_Sellers(info)
  
  def resolve_Products(self, info, name = None, category = None, sellerIdentifier = None):
    return resolve_Products(info)

  def resolve_Cart(self, info, id = None):
    return resolve_Cart(info, id)

  def resolve_Carts(self, info, sellerId = None, buyerId = None, status = 0):
    return resolve_Carts(info, sellerId, buyerId, status)

  def resolve_Buyers(self, info):
    return resolve_Buyers()

class Mutations(graphene.ObjectType):
    open_cart = OpenCart.Field()
    close_cart = CloseCart.Field()
    add_product = AddProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
