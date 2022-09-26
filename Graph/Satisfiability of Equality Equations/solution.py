class UF:
    def __init__(self):
        self.p = [i for i in range(26)]
    
    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        self.p[v] = u
        
    def same_group(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return True
        return False

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = UF()
        for eq in equations:
            u, sign, v = ord(eq[0]) - ord('a'), eq[1:3], ord(eq[3]) - ord('a')
            if sign == "==":
                equal.union(u, v)
        
        for eq in equations:
            u, sign, v = ord(eq[0]) - ord('a'), eq[1:3], ord(eq[3]) - ord('a')
            if sign == "!=":
                if equal.same_group(u, v):
                    return False
        return True
                
            
