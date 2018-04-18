import graphene
from lib.utils import normalize_field

class Buyer(graphene.ObjectType):
  id = graphene.String()
  identifier = graphene.String()
  name = graphene.String()

def format_buyer(data):
  buyer = Buyer()
  for key, value in data.items():
    buyer.__setattr__(normalize_field(key), value)
    
  return buyer