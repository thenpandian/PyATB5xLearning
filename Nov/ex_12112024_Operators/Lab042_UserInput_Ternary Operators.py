# Program= if age >18 - allowed to vote
#   else--> not allowed to vote


user_input_age= int(input("Enter your Age : \n"))

print("Your age is : ",user_input_age)

if user_input_age > 18:
    print("Your Allowed to vote")
else :
    print("Your not allowed to vote, since your age is",user_input_age)

# Ternary operator example

# print("Your Allowed to vote" if user_input_age > 18 else "Your not allowed to vote" )
# print("Your Allowed to vote" if int(input("Enter your Age : \n")) > 18 else "Your not allowed to vote" )
