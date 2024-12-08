# Take a input and create a class in python

class Person:


    def __init__(self):
        print("I will be Created")
        self.name = input("Enter the name \n")
        self.age =  input("Enter the age \n")
        self.phone = input ("Enter your Phone no \n")
        self.occupation = input("Enter your occupation \n")

    def name_of_the_fucntion_to_display(self):
        print(f"Name is {self.name}",f"Age is {self.age}",f"Your Phone No {self.phone}",
              f"Occupation is {self.occupation}")


person_ref = Person()
# person_ref.name_of_the_fucntion_to_display()