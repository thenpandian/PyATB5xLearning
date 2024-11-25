# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

# Logic Forumla

# Step 1
# user input -> input
# output --> Output

# Step 2 Rough Logic
# s1=S2=S3 -->equilateral
# s1=s2 or s2=s3 or s1=s3 --> isosceles
# s1!=s2 or s2!=S3 or S1!=S3  -- > scalene

def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b >c:
            if a == b == c:
                print("Its a Equilateral")
                return "Equilateral"
            elif a == b or a == c or b == c:
                print("Its a Isosceles")
                return "Isosceles"
            else:
                print("Its a scalene")
                return "scalene"
        else:
            print("Not a Triangle")
    else:
        print("Not a valid Length")


side1 = float(input("Enter the first side \n"))
side2 = float(input("Enter the Second side \n"))
side3 = float(input("Enter the Third side \n"))

result = classify_triangle(side1, side2, side3)
print("The triangle is classified", result)
