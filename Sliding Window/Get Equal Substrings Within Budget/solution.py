class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        cost = 0
        result = 0
        for end in range(n):
            cost += abs(ord(s[end]) - ord(t[end]))
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            result = max(result, end - start + 1)
        return result

