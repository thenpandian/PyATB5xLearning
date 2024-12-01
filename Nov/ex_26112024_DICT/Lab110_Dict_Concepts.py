# Dictionary from two lists

keys=["name","role","experience"]
values  = ["Pandian","SDET","35"]


my_dict = dict(zip(keys,values))
print(my_dict)


keys1=["name","role","experience"]
values1  = ["Pandian","SDET"]


my_dict1 = dict(zip(keys1,values1))
print(my_dict1)


keys2=["name","role"]
values2  = ["Pandian","SDET","35"]

my_dict2 = dict(zip(keys2,values2))
print(my_dict2)


#Merge two Dictionaries      |

dict1 = {"emp":"101","name":"Varun","Role":"SDET"}
dict2 = {"country":"India","city":"chennai","pincode":600091}

print(dict2)

merged_dict= dict1 | dict2

print(merged_dict)

# how to get the element -- get  instance
print(merged_dict["emp"])

print(merged_dict.get("emp"))