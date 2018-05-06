import os

class Buyer:
  @classmethod
  def get_results(cls):
    import requests
    url = "{0}:{1}/".format(os.environ['SANIC_BUYERS_SERVICE_HOST'], os.environ['SANIC_BUYERS_SERVICE_PORT'])
    response = requests.get(url=url)
    return response.json()