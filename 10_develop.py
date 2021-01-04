import requests 
# target = "http://google.com"
# response = requests.get(url=target)
# print(response.text)

import json

user = {
    "id" : "gildong",
    "password" : "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}

json_data = json.dumps(user, indent = 4)
print(json_data)

with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

#from json to python object
data = response.json()

name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)