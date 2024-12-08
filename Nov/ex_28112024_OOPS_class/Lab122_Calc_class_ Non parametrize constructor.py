
class Calc:


    def __init__(self):
        print("Data Calculator")


    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b


calc_ref = Calc()
a = float(input("Enter the value of a : \n"))
b = float(input("Enter the value of b : \n"))
output_sum = calc_ref.sum(a, b)
output_sub = calc_ref.sub(a, b)
output_mul = calc_ref.mul(a, b)
output_div = calc_ref.div(a,b)

print(output_sum,output_sub,output_mul,output_div)

output_sum1 = calc_ref.sum(10,10)
print(output_sum1)