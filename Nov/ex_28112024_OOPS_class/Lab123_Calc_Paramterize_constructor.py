class Calc():


    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return  self.a-self.b

    def mul(self):
        return  self.a * self.b

    def div(self):
        return  self.a/self.b

calc_ref= Calc(5,5)
# calc_ref.sum(5,5)
print(calc_ref.sum(),calc_ref.sub(),calc_ref.mul(),calc_ref.div())
