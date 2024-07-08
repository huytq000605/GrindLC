class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        empty = 0
        while numBottles:
            result += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return result
