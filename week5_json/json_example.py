import json


person = {}

person["name"] = "andy"
person["age"] = 41

for _ in person:
    print(_, person[_])
    
person["age"] = 42
    

for _ in person:
    print(_, person[_])
    
#save to json fil
json.dump(person, open("/home/ubuntu/environment/example.json", "w"))

age = 41
age = 42
age = 41

var = 2
for i in range(2, 20):
    var = var ** i
    print(var)
    
    
