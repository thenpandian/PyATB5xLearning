# Leap Year
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

year = int(input("Enter the Year : \n"))

def check_leap_year(year):
    if (year % 4==0 and year % 100 !=0) or (year % 400 ==0):
        return True
    else:
        return False



if check_leap_year(year):
    print("Its Leap Year")
else:
    print("Its not Leap Year")