class Solution:
    def numberOfWays(self, s: str) -> int:
        total_0 = 0
        total_1 = 0
        for l in s:
            if l == "0":
                total_0 += 1
            else:
                total_1 += 1
        result = 0
        left_0 = 0
        left_1 = 0
        for l in s:
            if l == "0":
                result += left_1 * (total_1 - left_1)
                left_0 += 1
            else:
                result += left_0 * (total_0 - left_0)
                left_1 += 1
        return result