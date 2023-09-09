class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        n = len(word)
        result = 0
        start = 0
        for i in range(n):
            for j in range(0, 11):
                if i - j < start: break
                if word[i-j:i+1] in forbidden:
                    start = i-j+1
                    break
            result = max(result, i - start + 1)
        return result
