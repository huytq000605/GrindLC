class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        cur = 0
        n = len(s)
        for i in range(n):
            if i >= k and s[i-k] in "ueoai":
                cur -= 1
            if s[i] in "ueoai":
                cur += 1
            result = max(result, cur)
        return result
