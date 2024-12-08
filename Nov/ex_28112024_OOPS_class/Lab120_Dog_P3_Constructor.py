# Class doesn't take memory
# Object take memory


class Dog:
    # Attribute  | Instance variable | Data Variables
    name = None
    breed = None
    height = None

    # In Java name of the constructor and class name should be same, but in Python (__init__)
    def __init__(self, name,breed):  # Parameterize Constructor     #  Constructor - its a special function in a class it will be automaticall when object is created
        print("Parameterized Constructor")
        self.name = name
        self.breed = breed

    # Behaviour
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleeping-> " + self.name)

    def talk(self):
        pass


# Create object
# Object Ref
chow_ref = Dog("chow","breed1")
lab_ref  = Dog("Labby","Husky")


print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))

print(lab_ref.name)
lab_ref.sleep()
print(id(lab_ref))

# Dog()   #  this is also object but no reference