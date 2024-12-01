# Find the missing key between two dictionaries

dict1 = {"a":1,"b":2,"c":3}

dict2 = {"a":1,"b":2}

missed_keys = dict1.keys()- dict2.keys()
print(missed_keys)


missed_keys1 = set(dict1.values())- set(dict2.values())
print(missed_keys1)


# Sort  a dictionary by its values in descending order


my_dict = {'a': 2, 'e': 5, 'd': 1, 'c': 7, 'b': 3}
print(my_dict)

sort_dict= sorted(my_dict.items())
sort_dict1= sorted(my_dict.keys())
sort_dict2= sorted(my_dict.values(),reverse=True)
print((sort_dict))
print((sort_dict1))
print((sort_dict2))