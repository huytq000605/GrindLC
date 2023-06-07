class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        for i in range(30):
            if (c >> i) & 1:
                if ((a | b) >> i) & 1 == 0:
                    result += 1
            else:
                if (a >> i) & 1:
                    result += 1
                if (b >> i) & 1:
                    result += 1
        return result
