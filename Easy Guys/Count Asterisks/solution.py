class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        result = 0
        for l in s:
            if count % 2 == 0 and l == "*":
                result += 1
            if l == "|":
                count += 1
            
        return result