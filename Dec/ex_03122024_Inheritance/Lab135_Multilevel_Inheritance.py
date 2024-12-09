# MultiLevel Inheritance

# GF -Father-Son


class Grandfather():
    gold = "2Kg"


    def bhk1(self):
        print("1 BHK")

class Father(Grandfather):
    diamond = "Diamond"

    def BHK2(self):
        print("2 BHK")

class Son(Father):
    Bit = "1000 Bitcoin"

    def BHK3(self):
        print ("3 BHK")


gf_obj = Grandfather()

fat_obj = Father()

son_obj = Son()

print(son_obj.gold)
son_obj.bhk1()
son_obj.BHK2()
son_obj.BHK3()


print("___")

fat_obj.bhk1()