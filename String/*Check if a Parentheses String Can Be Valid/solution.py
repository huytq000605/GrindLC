class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1: return False
        min_diff, max_diff = 0, 0
        for i in range(len(s)):
            if locked[i] == '0':
                min_diff -= 1
                max_diff += 1
            else:
                if s[i] == '(':
                    min_diff += 1
                    max_diff += 1
                elif s[i] == ')':
                    min_diff -= 1
                    max_diff -= 1
            if max_diff < 0: return False
            min_diff = max(min_diff, 0)
        return min_diff == 0
