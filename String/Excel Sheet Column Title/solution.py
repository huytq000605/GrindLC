class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n:
            n -= 1
            s += chr(n % 26 + ord('A'))
            n //= 26
        return s[::-1]
