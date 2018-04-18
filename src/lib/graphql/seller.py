import graphene
from lib.model.seller import Seller as SellerModel
from lib.model.product import Product as ProductModel
from lib.graphql.product import Product, resolve_Products, format_products
from lib.utils import normalize_field

class Seller(graphene.ObjectType):
  id = graphene.String()
  identifier = graphene.String()
  shortName = graphene.String()
  fullName = graphene.String()
  Products = graphene.List(lambda: Product)

def resolve_Sellers(info):
  return map(format_seller, SellerModel.get_results(info.root_value.json['query']))

def format_seller(data):
  seller = Seller()
  for key, value in data.items():
    if key == 'Products':
      seller.Products = format_products(data['Products'])
    else:
      seller.__setattr__(normalize_field(key), value)
    
  return seller