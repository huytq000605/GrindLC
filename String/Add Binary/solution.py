class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        plus = 0
        result = ""
        for i in range(max(m, n)):
            x,y = 0, 0
            if n - 1 - i >= 0:
                x = int(a[n-1-i])
            if m - 1 - i >= 0:
                y = int(b[m-1-i])
            result += str((x+y+plus) % 2)
            plus = (x+y+plus) // 2
        if plus > 0:
            result += "1"
        return result[::-1]