# Local variable can accessed directley without "Self"
# instance variable can be accessed by "self"
# Local variable always high preceedence as compared to global variable

a = 10 # Global variable


class person:
    b = 11    # Instance variable created under class


    def print_info(self):
        c = 20   # local variable
        print(c)   # Local variable can accessed directley without "Self"
        print(self.b)   # instance variable can be accessed by "self"
        a = "Hello"
        print(a)   # Local variable always high preceedence as compared to global variable
                        # we can use global a 


object_ref = person()
object_ref.print_info()