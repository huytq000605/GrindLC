class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        a = b = c = d = 0
        result = 0
        for ch in s:
            if ch == 'N':
                a += 1
            elif ch == 'S':
                b += 1
            elif ch == 'W':
                c += 1
            elif ch == 'E':
                d += 1
            add = max(a, b) + max(c, d)
            subtract = min(a, b) + min(c, d)
            result = max(result, add + min(k, subtract) - max(0, subtract - k))

        return result
