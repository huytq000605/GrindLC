class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        cur = 0
        coins.sort()
        # cur is the max target we can make (and we've made all value from 0 to cur)
        # to make (cur + 1) we need a new num that have value <= (cur + 1)
        # cur = cur + value
        for coin in coins:
            if coin > cur + 1:
                break
            cur += coin
        return cur + 1
