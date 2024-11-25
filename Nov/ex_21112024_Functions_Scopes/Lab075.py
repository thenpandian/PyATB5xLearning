pb_a = 12  # Global Variable


def my_function():
    pb=10  # Local Variable
    print(pb)
    print(pb_a)


# print(pb)  # Local variable can't called outside
my_function()
print(pb_a)
