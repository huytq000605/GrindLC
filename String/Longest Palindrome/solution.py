class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        result = 0
        left = 0
        for c, v in counter.items():
            result += v // 2 * 2
            left = max(left, v % 2)
        return result + left
