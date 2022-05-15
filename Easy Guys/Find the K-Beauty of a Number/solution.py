class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        result = 0
        for i in range(0, n-k+1):
            j = int(s[i:i+k])
            if j != 0 and num % j == 0:
                result += 1
        return result