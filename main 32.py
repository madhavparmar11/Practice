# ques --> create a class acount with functioning
# of account debit and credit functions?


class account:
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no

        def debit(self):
            amount = int(input("enter the debitted amount: "))
            print("current balance is: ", self.bal)
            db = slef.bal - amount
            print("now th total balance is : ", db)

        def credit(self):
            amount1 = int(input("enter the credited amount: "))
            print("the current balance is: ", db)
            cd = db + amount1
            print("the updated balance is: ", cd)

        def balance(self):
            print("the total balance is: ", cd)

        s1 = account()
        s1.debit
        s1.credit
        s1.balance
