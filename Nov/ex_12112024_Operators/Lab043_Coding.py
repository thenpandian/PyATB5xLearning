# Write the program to calculate the
#area of a cycle given its radius using the formula
#''' area=π* r^2'''(Take pie as 3.14)

# Logic Building Formula

# ||Step 1 ||
# Figure out the input and output
#input -> r --> datatype-->float
#pi = 3.14
# ^ -->** or math.pow --> two options we can use for
# Output --> float - area , print area


# ||Step 2||
# rough logic  = area = 3.14 * pow(r,2)

# ||Step3 ||

radius = float(input("Enter the raidus\n"))
print(radius)
area = 3.1456464446 * (radius ** 2)
print("Area of the circle is : ",area)
print(f"Area of the circle is {area}")  # difference of using  f--> formatting
print(f"Area of the circle is {area:.2f}")   # --> .2f states how many decimal after dot(.)


#* --> mul
# ** --> pow
print("---------------------------------------")
import math

print(math.pi)
print(math.pow(radius,2))
area = math.pi * (math.pow(radius,2))
print("Area of the circle is",area)

print("--------")
# program in one line

print(3.1456464446 * (radius ** 2))
print(3.1456464446 * (float(input("Enter the raidus\n")) ** 2))


print("---------------------")
#different math model

import math
print(math.pow)
print(math.pi)
print(math.cos(90))
print(math.sin(90))
print(math.factorial(5))