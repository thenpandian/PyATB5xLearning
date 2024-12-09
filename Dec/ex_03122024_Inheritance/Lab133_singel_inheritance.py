# How to create a class

# single inheritance--? 85% of time  we will use Single Inheritance in API

class Father:
    key="2BHK"  # Instance Variable

    def car(self):
        print("Father has a car --> Alto")
        print(self.key)



class Son(Father):    # used the father class inside the bracket - this single inheritance
    key1="3BHK"

    def suv(self):
        print("Son has a Creta ,Black")
        print(self.key1)


father_object = Father()
father_object.car()

son_obj = Son()
son_obj.suv()

son_obj.car()  # Calling the function from father class


# father_object.suv() this can't be used since it is father class