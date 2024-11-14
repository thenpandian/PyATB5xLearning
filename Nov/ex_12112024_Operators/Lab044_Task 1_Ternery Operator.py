# Write a program  to take a user age  and let him know if  he can go to  the club 21


# Logic Building Formula

# Step 1
# User Input -> Data type ->int
#output ->String-->User if he can go to the clue or not


# Step 2 , Rough Logic ( Brute force logic)
#age  > 21 -- > Print he can go to the club
#age < 21  --> Print he can't go to the club

#Step 3,Write the logic

user_age= int(input("Enter your age\n"))

if user_age>=21 :
    print("You are allowed in Club")
else :
    print(f"You are not allowed inside the club since your age is {user_age}")

# Step 4,Check for edge cases
# To identify when the program will failed
# we should consider edge cases such as :
# Negative ages or extemely high values --> program will break
#Non-numeric input -ABC
#Age which is valid





# Step 5, Optimize the code
# Handle all the ege cases




print("----------Ternary Operator-------")
print("You are allowed in Club" if user_age>=21 else "You are not allowed inside the club")