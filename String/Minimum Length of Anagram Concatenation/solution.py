class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        def valid(m):
            c1 = Counter(s[:m])
            for i in range(m, n, m):
                c2 = Counter(s[i:i+m])
                if len(c1) != len(c2) or any(c not in c2 or c1[c] != c2[c] for c in c1.keys()):
                    return False
            return True
            
        for m in range(1, n//2+1):
            if n % m != 0: continue
            if valid(m): return m
        return n
