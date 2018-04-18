import graphene
from lib.model.product import  Product as ProductModel
from lib.utils import normalize_field

class Product(graphene.ObjectType):
  id = graphene.String()
  sellerIdentifier = graphene.String()
  name = graphene.String()
  code = graphene.String()
  categories = graphene.List(graphene.String)

def resolve_Products(info):
  return format_products(ProductModel.get_results(info.root_value.json['query']))

def format_product(data):
  product = Product()
  for key, value in data.items():
    product.__setattr__(normalize_field(key), value)
    
  return product

def format_products(products):
  response = []
  for product in products:
    obj = format_product(product)
    response.append(obj)
  
  return response
