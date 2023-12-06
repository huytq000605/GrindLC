class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        money = 1
        day = 0
        while n:
            result += (money + day)
            day += 1
            if day == 7:
                day = 0
                money += 1
            n -= 1
        return result
