# Problem to find the Max  between 3 numbers


# Logic Building

# user inputs- num1 , num2,num3- int
#output--> int or string  with max number

# Logic ? if else - 1 condition,

# syntax
# if condition 1:
#print("do 1")
#elif condition 2:
#print(" print 2")
#elif condition 3:
# print("print 3")_
#else :
#print(" Do for else")

num1= int(input("Enter the value 1 : ")) # 5,# 10
num2= int(input("Enter the value 2 : ")) #3,# 12
num3= int(input("Enter the value 3 : ")) #2 .# 11

# 5 > 3 and 5 > 2 --> 5
#num1 > num2 and num1>num3 --> num1 is greater

# 12 > 10  and 12 > 11 --> true--> 12
#num2 > num1 and num2 > num3 --> num2 is greater

# if both above is false then in default num3 will be greater

if num1 > num2 and num1 > num3:
    print("Max value is num1",num1)
elif num2 > num1 and num2 > num3:
    print("Max value is num2",num2)
else:
    print("Max value is num3",num3)


