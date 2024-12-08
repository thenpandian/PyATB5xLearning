# Class doesn't take memory
# Object take memory


class Dog:
    # Attribute
    name = None
    breed = None
    height = None


    #Behaviour
    def bark(self):
        print("Barking")

    def sleep(self):
        print("sleeping")

    def talk(self):
        pass

# Create object
# Object Re
bulldog = Dog()
# Dog()-- Object
# bulldog --> Object_ref
bulldog.name = "Johny"

chow = Dog()
lab =  Dog()
chippi = Dog()