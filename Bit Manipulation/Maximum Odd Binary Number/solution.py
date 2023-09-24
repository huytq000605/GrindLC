class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')
        ones -= 1
        return '1' * ones + (n - 1 - ones) * '0' + '1'
