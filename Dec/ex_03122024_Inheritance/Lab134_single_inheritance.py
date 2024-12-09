class  Parent:
    gold = "2Kg"

    def __init__(self):    #constructor
        print("DC-Parent")

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"

    def __init__(self):     # Default Constructor
        print("Default constructor--child")

    def BHK3(self):
        print("3BHK")

child_obj = Child()
print(child_obj.gold)

print(child_obj.diamond)

child_obj.BHK3()
child_obj.BHK2()


parent_obj = Parent()
parent_obj.BHK2()