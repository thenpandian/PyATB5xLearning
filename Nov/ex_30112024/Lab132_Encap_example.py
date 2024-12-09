class Bank:


    def __init__(self,op_account_number,op_balance):
        self.balance = op_balance  # public
        self.__account_number = op_account_number # private

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount

    def show_acct_number(self,is_athen):     # To access private variable outside the class, call only thru functions
        if is_athen == True :
            print(self.__account_number)
        else :
            print("Not Allowed")


    def __internal_private_method(self):
        print("Private Method ,can be access  by only within class")


icici = Bank(525565556,500)
icici.check_balance()

print("----------")

icici.deposit(200)
icici.check_balance()
print(icici.balance)  # we can access the class variable since its public in nature

# print(icici.__account_number) # We cannot access since it is private
icici.show_acct_number(True)
icici.show_acct_number(False)