class Bankaccount:
    def __init__(self, in_rate, balance):
        self.in_rate = in_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrow(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance: we'ra taking £5 from u")
            self.balance -= 5
        return self
     
    def dispaly_account_info(self):
        print(f"Account balance: £{self.balance}")
        return self 
    
    def yield_interset(self):
        if self.balance > 0:
            self.balance += self.balance * self.in_rate
        return self
    
account1 = Bankaccount(0.02, 100)
account2 = Bankaccount(0.03, 100)

account1.deposit(50).deposit(100).deposit(25).withdrow(75)
account2.deposit(100).deposit(500).withdrow(750).withdrow(250).withdrow(200).withdrow(100).yield_interset()
account1.dispaly_account_info()
account2.dispaly_account_info()