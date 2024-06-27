class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        result = 0
        for c in s:
            if c == 'E':
                chairs += 1
            else:
                chairs -= 1
            result = max(result, chairs)
        return result
