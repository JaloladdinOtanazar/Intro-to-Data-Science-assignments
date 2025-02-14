def typeBasedTransformer(**kwargs):
 new_values = {}
 for  name, value in kwargs.items(): 
  if type(value) == int or type(value) == float:
   new_values[name] = value ** 2
  elif type(value) ==str:
   new_values[name] = value[::-1]
  elif type(value) == bool:
   if value == True:
    new_values[name] = False
   else:
    new_values[name] = True
  elif type(value) == tuple or type(value) == list:
   new_values[name] = value[::-1]
  elif type(value) == dict:
   new_values[name]  = {n: v for v, n in value.items()}
  else:
   new_values[name] = value
 return new_values
print(typeBasedTransformer(a = 12, b = "I am", c = True, d = [34,6,4], e = {"f": 45 ,"h": 65}))