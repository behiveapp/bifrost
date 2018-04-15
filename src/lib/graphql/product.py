import graphene
from sanic import Sanic
from lib.model.product import  Product as ProductModel

class Product(graphene.ObjectType):
  sellerIdentifier = graphene.String()
  name = graphene.String()
  code = graphene.String()
  categories = graphene.List(graphene.String)

def resolve_Products(info):
  return map(__format_product, ProductModel.get_results(info.root_value.json['query']))

def __format_product(data):
  product = Product()
  for key, value in data.items():
    product.__setattr__(key, value)
    
  return product
