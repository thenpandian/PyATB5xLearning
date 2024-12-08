# Class doesn't take memory
# Object take memory


class Dog:
    # Attribute
    name = None
    breed = None
    height = None


 # In Java name of the constructor and class name should be same, but in Python (__init__)
    def __init__(self):     #  Constructor - its a special function in a class it will be automaticall when object is created
        print("I will be called")

    #Behaviour
    def bark(self):
        print("Barking")

    def sleep(self):
        print("sleeping")

    def talk(self):
        pass

# Create object
# Object Re
bulldog_ref = Dog()
# Dog()-- Object
# bulldog --> Object_ref
bulldog_ref.name = "Johny"

chow_ref = Dog()
lab_ref =  Dog()
chippi_ref = Dog()

print(chippi_ref.name)
print(chow_ref.name)