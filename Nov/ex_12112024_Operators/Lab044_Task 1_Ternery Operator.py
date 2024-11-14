# Write a program  to take a user age  and let him know if  he can go to  the club 21

user_age= int(input("Enter your age\n"))

if user_age>=21 :
    print("You are allowed in Club")
else :
    print(f"You are not allowed inside the club since your age is {user_age}")


print("----------Ternary Operator-------")
print("You are allowed in Club" if user_age>=21 else "You are not allowed inside the club")