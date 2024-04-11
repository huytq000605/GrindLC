class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        l = len(s)
        for i in range(l-1):
            if s[i] > s[i+1]:
                break
        else: return n
        while i > 0 and s[i] == s[i-1]:
            i -= 1
        return int(s[:i] + str(int(s[i]) - 1) + '9' * (l - i - 1))
