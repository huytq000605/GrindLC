class Solution:
    def minimumLines(self, stocks: List[List[int]]) -> int:
        n = len(stocks)
        if n == 1:
            return 0
        stocks.sort()
        # (y3 - y2) / (x3-x2) = (y2 - y1) / (x2 - x1)
        # => (y3-y2)(x2-x1) = (y2-y1)(x3-x2)
        result = 1
        for i in range(2, n):
            x1, y1 = stocks[i-2]
            x2, y2 = stocks[i-1]
            x3, y3 = stocks[i]
            if (y3-y2)*(x2-x1) != (y2-y1)*(x3-x2):
                result += 1
        return result