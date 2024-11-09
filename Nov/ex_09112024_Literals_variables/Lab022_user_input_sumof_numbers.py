#Write a a program to take the 2 user input
#then sum the number
#mul-> *
#div -> /


# Logic Building
# Step 1
# I/P ->num1,numb2 -> int (DAA dont assume anything user mentioned that it is int)
# O/P sum - int, sub -> int, div ->float

# step 2 input accpets it as string ,so we need to convert the string to int using int(), float()

num1 = int(input("Enter the num 1 "))
num2 = int(input("Enter the num 1 "))

#num1 = int(num1)
#num2= int(num2)

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#Step 3
print("Sum is : ", sum)
print("Sub is : " ,sub)
print("Mul is : " , mul)
print("Div is : ", div)