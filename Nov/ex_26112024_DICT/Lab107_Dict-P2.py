student_infor ={
    "name" : "Thenpandian",
    "age" : "43",
    "address" : "TN"
}


print(student_infor["name"])
print(student_infor["age"])
student_infor["age"]=42
print(student_infor)

# different way Create 2nd Dictionary

student_infor2=dict(name="Muruga",age="35",address="TN")
print(student_infor2)

# Dictionary withing dictionary

student_infor2 ={
    "name" : "Thenpandian",
    "age" : "43",
    "address" : {
        "Home_Address":"Velachery",
        "pincode":"600091"
    }
}


print(student_infor2)