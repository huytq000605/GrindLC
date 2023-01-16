class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            if u > v:
                u, v = v, u
            self.p[v] = u
                

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        uf = UF(26)
        for i in range(n):
            i1 = ord(s1[i]) - ord('a')
            i2 = ord(s2[i]) - ord('a')
            uf.union(i1, i2)
        
        result = ""
        for c in baseStr:
            result += chr(uf.find(ord(c) - ord('a')) + ord('a'))
        return result
