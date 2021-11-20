class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        length = len(s)
        result = 0
        for i in range(1, length):
            result += len(digits) ** i
        def dfs(idx):
            if(idx >= length): return 1
            result = 0
            for digit in digits:
                if digit < s[idx]:
                    result += len(digits) ** (len(s) - idx - 1)
                elif digit == s[idx]:
                    result += dfs(idx + 1)
            return result
        result += dfs(0)
        return result