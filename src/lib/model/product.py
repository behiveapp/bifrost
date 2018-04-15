import os

class Product:
  @classmethod
  def get_results(cls, query):
    import requests
    url = "{0}:{1}/graphql".format(os.environ['SANIC_SHERLOCK_HOST'], os.environ['SANIC_SHERLOCK_PORT'])
    json = {"query" : query}
    response = requests.post(url=url, json=json)
    return response.json()['data']['Products']