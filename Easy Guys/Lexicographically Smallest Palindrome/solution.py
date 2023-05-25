class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        s = list(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                s[i] = chr(min(ord(s[i]), ord(s[n-1-i])))
                s[n-1-i] = s[i]
        return "".join(s)
