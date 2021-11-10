class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0, *balance]
        self.current = [0, *balance]
        
    def notValidMoney(self, account, money):
        if money < 0:
            return True
        return False
    
    def notValidAccount(self, account):
        if account < 1 or account >= len(self.balance):
            return True
        return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.notValidAccount(account1) or self.notValidAccount(account2):
            return False
        if self.notValidMoney(account1, self.current[account1] - money):
            return False
        self.current[account1] -= money
        self.current[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if self.notValidAccount(account):
            return False
        self.current[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.notValidAccount(account):
            return False
        if self.notValidMoney(account, self.current[account] - money):
            return False
        self.current[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)