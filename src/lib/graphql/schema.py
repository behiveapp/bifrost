import graphene
from lib.graphql.product import Product, resolve_Products
from lib.graphql.seller import Seller, resolve_Sellers
from lib.graphql.cart import Cart, resolve_Cart

class Query(graphene.ObjectType):
  Sellers = graphene.Field(graphene.List(lambda: Seller), name=graphene.String())
  Products = graphene.Field(graphene.List(lambda: Product), name=graphene.String(), category=graphene.String())
  Cart = graphene.Field(Cart, id=graphene.String())

  def resolve_Sellers(self, info, name):
    return resolve_Sellers(info)
  
  def resolve_Products(self, info, name = None, category = None):
    return resolve_Products(info)

  def resolve_Cart(self, info, id):
    return resolve_Cart(info, id)

schema = graphene.Schema(query=Query)
