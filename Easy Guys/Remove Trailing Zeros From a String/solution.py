class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i, d in enumerate(num[::-1]):
            if d != "0":
                return num[:len(num) - i]
        return ""
