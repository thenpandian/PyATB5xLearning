# Encapsulation mean hiding something
# Hide the Data members(class, variables,instance variables)
# by using only the methods


class Car:
    make =  None
    model = None
    password = "Pass123"

    def __init__(self):
        self.password = "pandian"
        self.__passowrd_secure = "muruga"  # private variable

    def change_password(self):
        print(self.__passowrd_secure)   # __private varibale can be used within only in the class and methods
        print(self.password)



car_ref = Car()
print(car_ref.password)
car_ref.change_password()
print(car_ref.__passowrd_secure)  #AttributeError: 'Car' object has no attribute '__passowrd_secure'. Did you mean: '_Car__passowrd_secure'?