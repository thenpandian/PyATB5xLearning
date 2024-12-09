# Web Automation - Selenium
# Page - You are going to automate


class VWOLoginPage:


    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "thenpandian@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else :
            print("Login Failed")

#email = Read from test data excel, csv or any file
#password = Read from test data excel or env file

email = input("Enter the email \n")
password = input("Enter your Password \n")


vwo_obj = VWOLoginPage(email,password)
vwo_obj.login_confirm()

# Directly passing the input value
# pandian_ref = VWOLoginPage("thenpandian@gmail.com","Pass123")
# pandian_ref.login_confirm()