import json

dct = {
    "name":"John",
    "age":30, 
    "city":"New York"
}

y = json.dumps(dct)

print(y)