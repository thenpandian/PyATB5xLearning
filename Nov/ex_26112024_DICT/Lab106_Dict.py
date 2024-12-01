# Key and Value Pair
# Dictionay is unordered, mutable, and indexed collection of key-value pairs in python
# It is defined by curly braces {}
# it will be used API automation

# common operations with dictionaries
# accessing values :my_dict[]
# adding/updating a key value pair: my_dict[key]= value
# Iterating:    for key, value in my_dict.items():

my_dict = {
    "name": "Pandian",
    "Age": 35,
    "Role": "Manual Tester",
    "Gender": "Male"
}

print(my_dict)
print(my_dict["Age"])
my_dict["Role"] = "SDET"
print(my_dict)

del my_dict["Age"]
print(my_dict)


# For   --> for key, value in my_dict.items():

for key,value in my_dict.items():
    print(key,"-->",value)


# Empty Dictionary


print("Age" in my_dict)
print("Role" in my_dict)



# Dictionary methods