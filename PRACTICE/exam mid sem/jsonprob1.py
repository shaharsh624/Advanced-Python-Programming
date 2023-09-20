import json

filename="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\data.json"

with open(filename,"r") as jsonfile:
    content=json.load(jsonfile)

print(content)