# Multiple Inheritance


class Father:

    def father_money(self):
        return 5

    def Home(self):
        return "This is Father Home"


class Mother:

    def mother_money(self):
        return 10

    def Home(self):
        return " This is Mother Home"


class Son(Father,Mother):   # First come First Serve

    def print_info(self):
        print("Son")


son_ob = Son()
print(son_ob.father_money())
print(son_ob.mother_money())
son_ob.print_info()

print(son_ob.Home())   # when both class is samee Function name, it will call the first function