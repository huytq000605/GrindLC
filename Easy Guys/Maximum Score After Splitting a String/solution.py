class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = s.count("1")
        result = 0
        zeros = 0
        for i in range(n-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            result = max(result, zeros + ones)
        return result
