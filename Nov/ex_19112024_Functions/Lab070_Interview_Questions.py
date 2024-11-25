# Create a program of sum of three number from the user input
# if user doesn't  enter any number, use default 100, 200,300,400

# Logic Building forumulas


num1=int(input("Enter the num1 : \n"))
num2=int(input("Enter the num2 : \n"))
num3=int(input("Enter the num3 : \n"))


def sum_three(n1=100,n2=200,n3=300):
    return n1+n2+n3

result= sum_three(num1,num2,num3)
print(result)


result2= sum_three()
result2= sum_three(10)
result2= sum_three(10,20)
result2= sum_three(30,30,30)
print(result2)
# We need to handle the Edge case ,user not enter anything