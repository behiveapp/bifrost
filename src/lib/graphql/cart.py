import graphene
from lib.model.cart import Cart as CartModel
from lib.graphql.buyer import Buyer, format_buyer
from lib.graphql.seller import Seller, format_seller
from lib.graphql.product import Product, format_products
from lib.utils import normalize_field


class Cart(graphene.ObjectType):
  id = graphene.String()
  createdAt = graphene.String()
  updatedAt = graphene.String()
  status = graphene.String()
  Buyer = graphene.Field(Buyer)
  Seller = graphene.Field(Seller)
  Products = graphene.List(lambda: Product)

def resolve_Cart(info, id):
  return __format_cart(CartModel.get_one(id))

def resolve_Carts(info, sellerId):
  return map(__format_cart, CartModel.from_seller(sellerId))

def __format_cart(data):
  cart = Cart()
  for key, value in data.items():
    if key == 'buyer':
      cart.Buyer = format_buyer(value)
    if key == 'seller':
      cart.Seller = format_seller(value)
    if key == 'products':
      cart.Products = format_products(value)
    else:
      cart.__setattr__(normalize_field(key), value)
    
  return cart