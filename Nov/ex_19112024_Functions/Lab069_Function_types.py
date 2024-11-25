# User Defined Functions
# 1. The can't return-> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters/ arguments
from wsgiref.util import request_uri

from Nov.ex_19112024_Functions.Lab064_Builtinfunctions import say_hello


# 1. The can't return-> non return
#No return type and No parameter/Argument- NRNP


def greet():
    print("Hello")

greet()

print("---------2nd Function Type -----------")
# No Return Type with and with Argument

def greet_by_name(name):
    print("Hello",name)

greet_by_name("Pandian")


print("---------No Return Type  and with default parameter -----------")

# 3.No Return Type  and with default parameter( # Positional Argument

# Default argument or positional Argument

def say_hi_default_argu(name="Thenpandian"):
    print("Hi",name.upper())

say_hi_default_argu("Palanisamy")
say_hi_default_argu()


print("---------No Return Type  and with default multiple arguments -----------")


def multiple_argu(name1="Thenpandian",name2="Muthamizh"):
    print("Multiple Argument",name1,name2)


multiple_argu()
multiple_argu("Dheepan")
multiple_argu("Palanisamy","Mangani")
multiple_argu(name1="Shirushti")
multiple_argu(name1="Muruga",name2="Namashivaya")
multiple_argu(name2="OmShakthi")


print("---------Argument + Retrun Type -----------")
# 4. Argument + Retrun Type

def sum_of_two(a,b):
    return a+b


result = sum_of_two(4,50)
print(result)

# with positional argument example

print("-------# with positional argument example----------")

def sum_of_two_number_with_default(num1=100,num2=200):
    return num1 +num2

result= sum_of_two_number_with_default(34,34)
print(result)

result= sum_of_two_number_with_default()
print(result)
