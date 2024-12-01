student_infor1 = {
    "name": "Shiva",
    "age": "32",
    "address": {
        "Home_Address": "Puzhuthivakam",
        "pincode": "600092"
    }
}

student_infor2 = {
    "name": "Muruga",
    "age": "33",
    "address": {
        "Home_Address": "Velachery",
        "pincode": "600091"
    }
}

print(student_infor1["address"]["Home_Address"])

student_list = [student_infor2, student_infor1]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["address"])
print(student_list[0]["address"]["pincode"])


# index value only work with list