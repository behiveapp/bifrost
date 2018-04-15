import graphene
from sanic import Sanic
from lib.graphql.product import Product, resolve_Products
from lib.graphql.seller import Seller, resolve_Sellers

class Query(graphene.ObjectType):
  Sellers = graphene.Field(graphene.List(lambda: Seller), name=graphene.String())
  Products = graphene.Field(graphene.List(lambda: Product), name=graphene.String(), category=graphene.String())

  def resolve_Sellers(self, info, name):
    return resolve_Sellers(info)
  
  def resolve_Products(self, info, name = None, category = None):
    return resolve_Products(info)

schema = graphene.Schema(query=Query)
