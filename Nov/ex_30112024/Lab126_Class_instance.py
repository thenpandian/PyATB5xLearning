# Instance variable can be accessed by the self

class person:



    def __init__(self,o_name):   # parameterized constructor
        self.name =o_name


    def walk(self):    # function with class is called as method
        return self.name
        # print(f"walking {self.name}")


name1=person("Thenpandian")     # Creating two Objects
name2=person("Muruga")

print(name1.name)
print(name2.name)


print("who is walking",name1.walk())
print("Who is walking ",name2.walk())



