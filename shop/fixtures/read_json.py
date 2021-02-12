import json

with open('./shop_data.json') as f:
  data = json.load(f)

print(len(data))
#print(data)
