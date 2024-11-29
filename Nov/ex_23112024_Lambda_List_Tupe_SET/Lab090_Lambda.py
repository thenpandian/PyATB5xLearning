# Syntax: The syntax to create a lambda function is **lambda arguments: expression**.
# he lambda keyword is used to define the anonymous function, followed by a list of arguments,
# a colon, and an expression.
#
# **Arguments**: Like a **normal function**, a lambda function can accept any number of arguments
# but must have only one expression. The arguments are specified before the colon.
#
# **Expression**: The expression is executed and the **result is returned**
# when the lambda function is called. This expression is written after the colon.
#

#normal function

# def triple_me(num):
#     return num ** 3
#
# result = triple_me(2)
# print(result)


# lambda
result_l=lambda num:num ** 3      # num is argument ; num**3 expression
print(result_l(2))

# you cannot have multiple statement in lambda