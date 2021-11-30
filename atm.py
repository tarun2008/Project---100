class Atm(object):
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def BalanceEnquiry(self):
        print("Your account balance is : 10000")    
    def CashWithdrawl(self, amount):
        currentAmount = 10000-amount
        print("You withdrawed : " + str(amount) + "Your remaining balance is :" + str(currentAmount))
def main():
    cardNumber = input("Enter your card number : ")
    pin = input("Enter your pin : ")
    user = Atm(cardNumber, pin)
    print("What you want to do -> ")
    print("Press '1' for Balance Enquiry ")
    print("press '2' for Cash Withdrawl ")
    operation = int(input(""))

    if operation == 1:
        user.BalanceEnquiry()
    elif operation == 2:
        amount = int(input("Enter the amount : "))
        user.CashWithdrawl(amount)    
    else:
        print("Press either '1' or '2' ")

main()         