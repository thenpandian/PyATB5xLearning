# Leap Year
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

# Logic Formula

# Step 1
# userinput --> enter the year--> int
#output --> print Leap Year or not Leap year


year= int(input("Enter the Year : \n"))

# Step 2 Rough Logic
# year % 4 ==0 and year % 100 !=0
#  year % 400==0

if year % 4 ==0 and year % 100 !=0:
    print("It's a Leap Year")
elif year % 400==0 :
    print("A Leap Year")
else:
    print("It is not Leap Year")