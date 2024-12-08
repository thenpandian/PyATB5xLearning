class Dog:
    # Class attribute
    species = "Canine"

    # Constructor to initialize an object's attributes
    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute

    # Method (function) inside a class
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)  # dog 1 object reference
dog2 = Dog("Charlie", 5)

# Accessing attributes and methods
print(dog1.name)   # Output: Buddy
print(dog2.bark()) # Output: Charlie says Woof!
print(dog2.species)