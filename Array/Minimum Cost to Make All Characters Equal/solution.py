class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        pre = [0 for _ in range(n)]
        suf = [0 for _ in range(n)]
        
        cur = s[0]
        for i in range(n):
            if i > 0:
                pre[i] = pre[i-1]
            if s[i] != cur:
                pre[i] += i
                cur = s[i]
        
        cur = s[-1]
        for i in reversed(range(n)):
            if i < n-1:
                suf[i] = suf[i+1]
            if s[i] != cur:
                suf[i] += n-i-1
                cur = s[i]
        return min([pre[i] + suf[i] for i in range(n)])
