# List

# it is collection of items ; Duplicates are allowed in List

# syntax : always present in SQuare Bracket []

# example : butter, panneer, honey
# 10th marks - 90,91,92

my_list= [1,2,3] # same type of data
my_list2=[1,True,"Pandian",12.34] # can have multiple data types

print(my_list)
print(my_list2)
print(len(my_list2))

print(my_list2[0])
print(my_list2[1])
print(my_list2[2])
print(my_list2[3])
# print(my_list2[4])  #print     list index out of range

# we can rearrage the value in lst
my_list[0]= "Pandian"
my_list[1]= "Muruga"
print(my_list)


print("***************************")


for i in my_list:   # range is not required , since range itself print it as list
    print(i)

# in list we
print("------------------------------")
for i in range(1,5):   # range  (start,
    print(i, end="")