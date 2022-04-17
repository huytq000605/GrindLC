class ATM:

    def __init__(self):
        moneys = [20, 50, 100, 200, 500]
        self.money = [[0, moneys[i]] for i in range(5)]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, m in enumerate(banknotesCount):
            self.money[i][0] += m

    def withdraw(self, amount: int) -> List[int]:
        arr = [0 for i in range(5)]
        for i in range(4, -1, -1):
            times = min(self.money[i][0], amount // self.money[i][1])
            amount -= times * self.money[i][1]
            arr[i] = times
        if amount > 0:
            return [-1]
        else:
            for i in range(5):
                self.money[i][0] -= arr[i]
            return arr


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)