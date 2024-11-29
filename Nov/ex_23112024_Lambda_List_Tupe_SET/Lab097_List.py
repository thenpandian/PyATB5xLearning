my_list= [1,2,3]

print("Element at the Index 0 : ",my_list[0])
print("Element at the Index 1 : ",my_list[1])
print("Element at the Index 2 : ",my_list[2])



# append ()-- # append object  the end of the list
my_list.append(4)
my_list.append(5)
print(my_list)


# Extend   --> append a new list
my_list.extend([7,10,9,8])
print(my_list)

# insert --> insert element in the index
my_list.insert(1,"Pandian")
print(my_list)
print(len(my_list))

my_list[0]="Muruga"
print(my_list)

#remove
my_list.remove("Pandian")
print(my_list)
my_list.remove("Muruga")
#copy

my_copy_list = my_list.copy()
print(my_copy_list)

my_copy_list.sort()   # TypeError: '<' not supported between instances of 'int' and 'str'
print(my_copy_list)
print(my_list)