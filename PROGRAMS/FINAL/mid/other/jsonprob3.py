import json

filepath="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\data.json"

with open(filepath,"r") as jsonfile:
    data=json.load(jsonfile)

print(data)
print(data['person']['name'])
