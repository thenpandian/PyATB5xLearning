# Hierarchical Inheritance

class Father:


    def bhk1(self):
        print("1 BHK")


class son1(Father):

    def bhk2(self):
        print("2 BHK")

class son2(Father):


    def bhk3(self):
        print("3 BHK")



son1_obj = son1()
son2_obj = son2()

son1_obj.bhk1()

son2_obj.bhk1()