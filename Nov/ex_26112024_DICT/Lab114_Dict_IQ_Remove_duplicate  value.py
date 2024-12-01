# Remove duplicate values from dicitonary

my_dict={"a":1,"b":2,"c":1,"d":3}

#o/P {"a":1,"b":2,"d":3}

# unique_dict ={}
#
#
# for key,value in my_dict.items():
#     if value not in unique_dict.values():
#         unique_dict[key] = value
#
# print(unique_dict)


# Alternat Way

unique_value = set()

result = {}

for key,value in my_dict.items():
    if value not in unique_value:
        result[key]= value
        unique_value.add(value)


print(result)
print(unique_value)