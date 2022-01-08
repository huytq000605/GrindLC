class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 1
        start = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                result += 1 + (i-1 - start + 1)
            else:
                start = i
                result += 1
                
        return result