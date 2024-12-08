class person :
    # Attributes  # What you have ?
    id = None
    name = None
    age = None
    Gender = None
    email = None
    phoneno = None
    address = None


    # Behaviour   What you can do
        def talk(self):  #  NRNG (No return no argument)self- this, self will be first argument
            print("I can talk")

        def sleep(self,name):  # Arg with no return
            print("I am Method !")
            print("sleep",name)

        def sleep2(self,name):
            print("I am Method!!")
            return None


        def walk(self):
            print("I am walking")

        def walk_return:  # No Arg with return
            return "I am walking"


# Create an object for the class= object reference
#objectref = ClassName() -- > object
geeta = person()
geeta.name = "Geeta sharma"
geeta.gender = "Female"