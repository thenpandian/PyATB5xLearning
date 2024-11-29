
# Union
print("UNION")
set1 = {1,2,3,3,4}
set2 = {4,5,6}
my_set =  set1.union(set2)
print(my_set)


# Intersect
print("Inersection")
set3 = { 9,8,50.5,10,11,12}
set4 = {7,13,9,50.5,7}
my_set1 = set3.intersection(set4)
print(my_set1)


#Difference
print("Difference")

my_set2=set3.difference((set4))
print(my_set2)

my_set2=set4.difference((set3))
print(my_set2)