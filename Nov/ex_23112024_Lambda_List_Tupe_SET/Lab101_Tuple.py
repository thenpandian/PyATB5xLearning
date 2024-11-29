cities = ("London", "Paris", "Berlin", "Delhi")
print("Paris" in cities)
print("Chennai" in cities)

t = (12, 44, 44)  # to add new item we need to conver the tuple to list and then add it

my_list = list(t)  # converting the tuple to List using list() keyword
my_list.append(555)
print(my_list)
