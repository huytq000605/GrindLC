class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0]*26
        for c in s:
            count[ord(c) - ord("a")] += 1
        for c in t:
            count[ord(c) - ord("a")] -= 1
        result = 0
        for i in range(26):
            result += abs(count[i])
        return result