class Home:


    def __init__(self):
        self.pubic_var = "father"
        self.__private_var = "child"


    def mom(self):
        print(self.__private_var)
        print(self.__wife())

    def __wife(self):
        print("Private Wife")


object_ref = Home()
object_ref.mom()
print(object_ref.pubic_var)
