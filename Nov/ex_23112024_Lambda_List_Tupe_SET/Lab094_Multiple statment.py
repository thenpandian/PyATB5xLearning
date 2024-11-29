# Write  a program to calculate even and odd

#
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else :
#         print("Odd")
#
# find_even_odd(5)

# Lambda with Ternary Operator
n= int(input("Enter the number \n"))

check_even_odd = lambda num : "Even" if num % 2==0 else "Odd"   # : "Even" if num % 2==0 else "Odd" is ternary operator
print(check_even_odd(n))