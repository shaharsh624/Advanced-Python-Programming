import json
data={
    "name":"Tithi",
    "age":30,
    "city":"India"
}

filepath="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\data.json"

with open(filepath,"w") as jsonfile:
    json.dump(data,jsonfile)
