import graphene
from lib.model.buyer import Buyer as BuyerModel
from lib.utils import normalize_field

class Buyer(graphene.ObjectType):
  id = graphene.String()
  identifier = graphene.String()
  name = graphene.String()

def resolve_Buyers():
  return map(format_buyer, BuyerModel.get_results())

def format_buyer(data):
  buyer = Buyer()
  for key, value in data.items():
    buyer.__setattr__(normalize_field(key), value)
    
  return buyer