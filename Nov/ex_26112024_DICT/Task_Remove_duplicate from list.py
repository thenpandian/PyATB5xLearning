my_list = [1, 2, 2, 3, 4, 4, 5]


my_list_uni = list(set(my_list))   # converting the lis to Set and again set to list

print(my_list_uni)



# Alternate Way

# my_list_uni1 = []
# for item in my_list:
#     if item not in my_list_uni1:
#         my_list_uni1.append(item)
#
# print(my_list_uni1)
