# Function that returns the maximum value from a dicitonary
#{"a":10,"b":20,"c":30}


# my_dict = {"a":10,"b":20,"c":30}
#
#
# max= max(my_dict.values())
# print(max)


# Alternate way

def max_value_dict(dicitonary) :
    # return max(dicitonary.values())
    return min(dicitonary.values())


print(max_value_dict({"a":10,"b":20,"c":30} ))