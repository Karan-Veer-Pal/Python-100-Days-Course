# Day : 33 Dictionaries

# Python Dictionaries
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dic1 = {
  "Karan" : "Human Being",
  "Spoon" : "Utensil"
}
print(dic1["Karan"])

print("\n")

# Dictionary is a combination of key value pair.
# Syntax : "key" : "value"

dic2 = {
  344 : "Karan",
  56 : "Lokki",
  678 : "Avinash",
  567 : "Rishav"
}
print(dic2[56])

print("\n")

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# print(info["name2"]) # -> Error Through not exist name2 key
# print(info.get("name2")) # -> Through None

print("\n")

# Accessing Dictionary items:

print("How to access Dictionary:\n")

# I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

print("Accessing single values:")
print(info['name'])
print(info.get('eligible'))

print("\n")

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

print("Accessing multiple values:")
print(info.values())

print("\n")

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

print("Accessing Keys:")
print(info.keys())

print("\n")

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

print("Accessing key-value pairs:")
print(info.items())

print("\n")

# Using For Loop:

print("Using For Loop for accessing all keys:")
for key in info.keys():
  print(info[key])

print("\n")

# Using f=string:

print("Using f-string for accessing all keys:")
for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print("\n")

print("Using f-string for accessing all items:")
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")

print("\n")
