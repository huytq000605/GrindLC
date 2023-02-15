class Solution:
    def addToArrayForm(self, a: List[int], b: int) -> List[int]:
        b = list(map(int, list(str(b))))
        n, m = len(a), len(b)
        if m > n:
            n, m = m, n
            a, b = b, a
        
        c = 0
        for i in range(n):
            a[n-1-i] += c
            if m-1-i >= 0:
                a[n-1-i] += b[m-1-i]
            c = a[n-1-i] // 10
            a[n-1-i] %= 10
        if c:
            return [c] + a
        return a
