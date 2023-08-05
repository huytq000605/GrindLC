class Solution:
    def accountBalanceAfterPurchase(self, a: int) -> int:
        b = a // 10
        c = b + 1
        if (c * 10 - a) <= (a - b * 10):
            return 100 - c * 10
        else:
            return 100 - b * 10
