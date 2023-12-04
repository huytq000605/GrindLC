class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        target = n-1
        ops = 0
        for i in range(n-1, -1, -1):
            if s[i] == "1":
                ops += (target - i)
                target -= 1
        return ops
