class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        brackets = [[0, 0], *brackets]
        i = 1
        while income > 0:
            result += min(income, brackets[i][0] - brackets[i-1][0]) * (brackets[i][1]) / 100
            income -= min(income, brackets[i][0] - brackets[i-1][0])
            i += 1
        return result