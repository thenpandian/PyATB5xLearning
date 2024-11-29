t=tuple()
print(t)



t1=tuple(["Muruga",1,2,3,14])
print(t1)

list=[5.6,7,801,66,66,"Pandian"]
list1=["Angel","Shiva"]
new_list=[list1,list]
print(new_list)
print(list)
t2=tuple(list)
print(t2)

hero1= ("Batman","Superman","Flash")
hero2=("Iron Man","spiderman","HULK")
print(hero1)
new_tuple=(hero1,hero2)
print(new_tuple)
print(new_tuple[0])  #  O/P('Batman', 'Superman', 'Flash')


print(new_tuple[0][0])    # O/P Batman
print(new_tuple[1][1])   # o/P  spiderman