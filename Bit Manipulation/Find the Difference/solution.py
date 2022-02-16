class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for i in range(len(s)):
            xor ^= ord(s[i])
            xor ^= ord(t[i])
        xor ^= ord(t[-1])
        return chr(xor)
