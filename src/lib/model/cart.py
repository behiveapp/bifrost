import os
import requests

class Cart:
  @classmethod
  def get_one(cls, id):
    url = "{0}:{1}/{2}".format(os.environ['SANIC_CART_SERVICE_HOST'], os.environ['SANIC_CART_SERVICE_PORT'], id)
    response = requests.get(url=url)
    # import pdb; pdb.set_trace()
    return response.json() if response.ok else {}

  @classmethod
  def from_seller(cls, sellerId):
    url = "{0}:{1}/from-seller/{2}".format(os.environ['SANIC_CART_SERVICE_HOST'], os.environ['SANIC_CART_SERVICE_PORT'], sellerId)
    response = requests.get(url=url)
    return response.json() if response.ok else []

  @classmethod
  def open_cart(cls, buyer, seller):
    url = "{0}:{1}/".format(os.environ['SANIC_CART_SERVICE_HOST'], os.environ['SANIC_CART_SERVICE_PORT'])
    json = {"buyer": buyer, "seller": seller}
    response = requests.post(url=url, json=json)
    return response.json() if response.ok else []

  @classmethod
  def add_product(cls, cart_id, product_id):
    url = "{0}:{1}/{2}/product/{3}".format(os.environ['SANIC_CART_SERVICE_HOST'], os.environ['SANIC_CART_SERVICE_PORT'], cart_id, product_id)
    response = requests.post(url=url)
    return response.json() if response.ok else []