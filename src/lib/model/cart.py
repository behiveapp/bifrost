import os

class Cart:
  @classmethod
  def get_one(cls, id):
    import requests
    url = "{0}:{1}/{2}".format(os.environ['SANIC_CART_SERVICE_HOST'], os.environ['SANIC_CART_SERVICE_PORT'], id)
    response = requests.get(url=url)
    # import pdb; pdb.set_trace()
    return response.json()