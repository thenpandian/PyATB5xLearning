# Match Statement -- > equals to Switch Statement
# match the op and execute
# Python > 3.10



# match variable :
#   case pattern 1 :
    # code block
# case pattern 2:
    # code block
# case patter 3 :
    # code block

# Write a program  to ask the use which browser  he want to run the automation

browser_name= input("Enter the Browser Name \n")
match browser_name :
    case "firefox":
        print("Execute the Firefox")
    case "Edge":
        print("Execute th code in Edge")
    case "Safari":
        print("Execute the code in safari")
    case "chrome":
        print("Execute the Code in Chrome")
    case _:
        print("Browser Not Found")