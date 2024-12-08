class PyAtb():


    def __init__(self,name,age,role,gender,city):
        self.name =  name
        self.age = age
        self.role = role
        self.gender =gender
        self.city = city

    def charcter(self):
        print("Good Student",self.name)

    def batch(self):
        print("Is batch is")


pandian_ref = PyAtb("pandian","43","SDET","M","Chennai")
pramod_ref = PyAtb("Pramod","30","SDET","M","Gurugan")
print(pandian_ref.name,pandian_ref.age,pandian_ref.role,pandian_ref.gender,pandian_ref.city)
pandian_ref.charcter()
print(pramod_ref.name,pramod_ref.role,pramod_ref.age,pramod_ref.gender,pramod_ref.city)