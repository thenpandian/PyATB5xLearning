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
student_infor3 = {
    "name": "Moorthy",
    "age": "40",
    "address": {
        "Home_Address": "PONDI",
        "pincode": "600091",
        "office_address":"Chennai"
    }
}


print(student_infor3["address"]["office_address"])


stu_list=[student_infor1,student_infor2,student_infor3]

print(stu_list[2]["address"]["pincode"])