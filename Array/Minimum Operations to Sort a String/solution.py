class Solution:
    def minOperations(self, s: str) -> int:
        mx = max(s)
        mn = min(s)
        is_sorted = True
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
        if len(s) == 2:
            return -1
        if s[0] == mn or s[-1] == mx: return 1
        for i in range(1, len(s) - 1):
            if s[i] == mn or s[i] == mx: return 2
        return 3
