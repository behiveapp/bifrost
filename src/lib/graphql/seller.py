import graphene
from sanic import Sanic
from lib.model.seller import Seller as SellerModel
from lib.model.product import Product as ProductModel
from lib.graphql.product import Product, resolve_Products

class Seller(graphene.ObjectType):
  identifier = graphene.String()
  shortName = graphene.String()
  fullName = graphene.String()
  Products = graphene.List(lambda: Product)

def resolve_Sellers(info):
  return map(__format_seller, SellerModel.get_results(info.root_value.json['query']))

def __format_seller(data):
  seller = Seller()
  for key, value in data.items():
    if key == 'Products':
      seller.Products = __format_products(data['Products'])
    else:
      seller.__setattr__(key, value)
    
  return seller

def __format_products(products):
  response = []
  for product in products:
    obj = Product()
    for key, value in product.items():
      obj.__setattr__(key, value)
    response.append(obj)
  
  return response