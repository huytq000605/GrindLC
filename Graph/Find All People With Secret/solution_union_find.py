import collections

class UnionFind:
    def __init__(self):
        self.p = dict()
        self.people = collections.defaultdict(set)
        self.r = dict()
    
    def find(self, x):
        if x not in self.p:
            self.p[x] = x
            self.people[x] = set([x])
            self.r[x] = 1
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        x_p, y_p = self.find(x), self.find(y)
        if x_p != y_p:
            if self.r[x_p] < self.r[y_p]:
                x_p, y_p = y_p, x_p
            self.r[x_p] += self.r[y_p]
            self.p[y_p] = self.p[x_p]
            self.people[x_p].update(self.people[y_p])

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda meeting: meeting[2])
        result = set()
        result.add(0)
        result.add(firstPerson)
            
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            uf = UnionFind()
            knowSecret = set()
            while i < len(meetings) and meetings[i][2] == time:
                p1, p2, t = meetings[i]
                uf.union(p1, p2)
                i += 1
            for person in uf.people.keys():
                if person in result:
                    knowSecret.update(uf.people[uf.find(person)])
                        
            result.update(knowSecret)
            
        return result
        