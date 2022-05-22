class Solution:
    def minimumLines(self, stocks: List[List[int]]) -> int:
        n = len(stocks)
        if n == 1:
            return 0
        stocks.sort()
        # y = ax + b
        # 4 = 3a + b
        # 2 = a + b
        a = (stocks[1][1] - stocks[0][1]) / (stocks[1][0] - stocks[0][0])
        b = stocks[1][1] - a * stocks[1][0]
        result = 1
        for i in range(2, n):
            new_a = (stocks[i][1] - stocks[i-1][1]) / (stocks[i][0] - stocks[i-1][0])
            new_b = stocks[i][1] - new_a * stocks[i][0]
            print(a, b, new_a, new_b)
            if new_a != a or new_b != b:
                a, b = new_a, new_b
                result += 1
        return result