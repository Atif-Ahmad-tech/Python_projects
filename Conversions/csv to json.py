import json
#convert python divtionary to json
a= {'name': 'atif',
    'age': 20,
    'slalry':'20000'}
b = json.dumps(a)
print(b)

## 
print(json.dumps(["welcome",'to', "pakistan"]))