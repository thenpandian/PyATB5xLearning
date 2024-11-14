#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

# Logic Forumla

# Step 1
# user input -> input
#output --> Output

# Step 2 Rough Logic
# s1=S2=S3 -->equilateral
# s1=s2 or s2=s3 or s1=s3 --> isosceles
# s1!=s2 or s2!=S3 or S1!=S3  -- > scalene

s1= int(input("Enter the Side 1 :\n"))
s2= int(input("Enter the side 2 : \n"))
s3= int(input("Enter the side 3 : \n"))

if s1==s2 and s1==s3 and s2==s3 :
    print("Triangle is Equilateral")
elif s1==s2 or s1==s3 or s2==s3 :
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")