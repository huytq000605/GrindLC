class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if result and abs(ord(result[-1]) - ord(c)) == 32:
                result.pop()
            else:
                result.append(c)
        return "".join(result)
