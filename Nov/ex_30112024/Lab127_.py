class car:


    def __init__(self,o_name,o_make,o_model):
        self.name =o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting  a car with the name", self.name)
        print("Starting  a car with the make" + self.make)  # we can use "+"
        print("Starting  a car with the make", self.model)


lambo = car("Lambhorgini","V6","2023")   # Object
lambo.start_engine()


print("-------------")


mg_hector = car("MG_HECTOR","1.5 Turbo","2024")  # Object
mg_hector.start_engine()