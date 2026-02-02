class Account:
    def deposit(self):
        x , y = input().split()
        self.x = int(x)
        self.y = int(y)
    def withdraw(self):
        if self.y > self.x:
            print("Insufficient Funds")
        else :
            print(self.x - self.y)

obj = Account()
obj.deposit()
obj.withdraw()