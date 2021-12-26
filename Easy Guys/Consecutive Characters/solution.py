class Solution:
    def maxPower(self, s: str) -> int:
        result = 1
        current = 0
        prev = ""
        for l in s:
            if l == prev:
                current += 1
                result = max(result, current)
            else:
                current = 1
                prev = l
        return result
				