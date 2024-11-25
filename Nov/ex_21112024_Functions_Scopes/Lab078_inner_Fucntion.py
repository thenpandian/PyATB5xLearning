# Due to intendation function became child of parent function .indentation to group statements and blocks of code in Python

def outer_function():
    var1 = 30  # local variable

    def inner_function():
        var2 = 20
        print(var1)

        def inner_function1():
            print(var1)
            print(var2)

        inner_function1()
    inner_function()

    # print(var2)

outer_function()
