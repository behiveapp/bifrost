def underscore_to_camelcase(value):
  def camelcase(): 
    yield str
    while True:
      yield str.capitalize

  c = camelcase()
  return "".join(next(c)(x) if x else '_' for x in value.split("_"))

def normalize_field(field):
  value = field[1:] if field[0] == '_' else field
  return underscore_to_camelcase(value)