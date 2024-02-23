class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        result = [0 for _ in range(n)]
        cur = 0
        for i, d in enumerate(word):
            cur = cur * 10 + int(d)
            if cur % m == 0:
                result[i] = 1
            cur %= m
        return result
