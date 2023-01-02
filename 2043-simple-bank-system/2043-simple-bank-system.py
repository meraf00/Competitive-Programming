class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {}
        
        for account, money in enumerate(balance):
            self.balance[account + 1] = money
            
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.balance and account2 in self.balance:
            if self.withdraw(account1, money):
                return self.deposit(account2, money)
        return False
        
    def deposit(self, account: int, money: int) -> bool:
        if account in self.balance:
            self.balance[account] += money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if self.balance.get(account, -1) - money >= 0:
            self.balance[account] -= money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)