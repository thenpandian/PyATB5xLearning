# Multiple Inheritance

class A:


    def method(self):
        return "Method A"

class B:

    def method(self):
        return "Method B"


class C(B,A):   # We are calling B class first, so it will give precedence for B

    pass

c_oj = C()

print(c_oj.method())