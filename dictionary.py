#python dictionaries
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)
#dictionaries items
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  'number ':19234
}
print(dict1["brand"])
#duplicates are not allowed
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "num1":194,
  "num2":234
}
print(dict)
#dict len
print(len(dict))
#data types
dict = {
  "brand": "Apache",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(dict)
#Acces dict
x = dict.get("brand")
print(x)
#key


x = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

y = x.keys()

print(x) #before the change

x["color"] = "white"

print(y) #after the change
#values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#items
y = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = y.items()

print(x) #before the change

y["year"] = 2020

print(x) #after the change


#checking dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  'aravindh':"kannan",
  "year": 1964
}
if "aravindh" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#updating items in dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"aravindh date of birth": 2003})

#removing items in dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "aravindh":"kannan",
  "year": 1964
}
thisdict.pop("aravindh")
print(thisdict)
#poping a item in dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#clear a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "aravindh":"kannan"
}
thisdict.clear()
print(thisdict)
#Loops in dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "aravindh":"kannan"
}
for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)
for x ,y in thisdict.items():
  print(x)

#Copy dictionaries
t = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "aravindh":"kannan"
}
mydict = t.copy()
print(mydict)
#nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004,
  "dob":2003
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
child4 = {
    'aravindh' :'kannan'
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3,
  "child4":child4
}
