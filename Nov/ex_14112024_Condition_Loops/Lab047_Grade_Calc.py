# Grade Calculator
# Write  a program that caluclate    and displas  the letter grade for a given numerical one
# (A,B,C,D,E,F) base on the following  grading scale

# A : 90-100
# B :80-89
# C :70-79
# D :60-69
# F

# Logic Formula
# Step 1
# user input--> Score--> int
# Outpuut --> A or B --> String


# step 2 Rough Logic

score = int(input("Enter the Score : \n"))

##score  >= 90 and score <=100 --"A"
# score  >= 80 and score <=89 --"B"
# score  >= 70 and score <=79 --"C"
# score  >= 60 and score <=69 --"D"
# score  <60 -- > "F"

if score >= 90 and score <= 100:
    print("Your Grade is A")
elif score >= 80 and score <= 89:
    print("Your Grade is B")
elif score >= 70 and score <= 79:
    print("Your Grade is C")
elif score >= 60 and score <= 69:
    print("Your Grade is D")
elif score >=100 and score <=-1 :
    print("Wrong Input check the score")
else:
    print("You are Unsuccessful")
