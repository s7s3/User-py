class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposite(self,amount):
        self.account_balance+=amount
   
    def make_withdrawal(self, amount):
        self.account_balance-=amount


    def display_user_balance(self):

       print(f"the name of the user is {self.name} and the account balance is {self.account_balance}")

    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        self.account_balance-=amount

khlid=User("Khlid","khlid@gmail.com")
hossam= User("Hossam", "hossam@gmail.com")
ratyl= User("ratyl","ratyl@gmail.com")

hossam.make_deposite(100)
hossam.make_deposite(1000)
hossam.make_deposite(3000)
hossam.make_withdrawal(900)
hossam.display_user_balance()

khlid.make_deposite(2000)
khlid.make_deposite(2500)
khlid.make_withdrawal(600)
khlid.make_withdrawal(150)
khlid.display_user_balance()

ratyl.make_deposite(5000)
ratyl.make_withdrawal(200)
ratyl.make_withdrawal(300)
ratyl.make_withdrawal(1000)
ratyl.display_user_balance()

hossam.transfer_money(ratyl,3000)
ratyl.display_user_balance()
hossam.display_user_balance()