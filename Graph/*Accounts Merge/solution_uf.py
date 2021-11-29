class UnionFind:
    def __init__(self):
        self.emails = collections.defaultdict(set)
        self.p = dict()
        self.r = dict()
        
    def find(self, x):
        if x not in self.p:
            self.p[x] = x
            self.r[x] = 1
            self.emails[x].add(x)
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x,y):
        x_p, y_p = self.find(x), self.find(y)
        if x_p != y_p: 
        
            if self.r[x_p] < self.r[y_p]:
                x_p, y_p = y_p, x_p
            self.emails[x_p].update(self.emails[y_p])
            self.r[x_p] += self.r[y_p]
            self.p[y_p] = x_p
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = dict()
        uf = UnionFind()
        for account in accounts:
            name = account[0]
            emails = account[1:]
            n = len(emails)
            if n == 1:
                names[emails[0]] = name
                uf.find(emails[0])
            else:
                for i in range(n - 1):
                    names[emails[i]] = name
                    uf.union(emails[i], emails[i+1])
        result = []
        for x, x_p in uf.p.items():
            if x == x_p:
                result.append([names[x], *sorted(list(uf.emails[x]))])
        return result