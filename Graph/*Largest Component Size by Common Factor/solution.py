class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for i in range(n)]
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        x_p, y_p = self.find(x), self.find(y)
        if x_p != y_p:
            if self.r[x_p] < self.r[y_p]:
                x_p, y_p = y_p, x_p
            self.r[x_p] += self.r[y_p]
            self.p[y_p] = x_p
        

class Solution:
    def getPrimes(self, n):
        result = set([n])
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n // i)
        return result
    
    def largestComponentSize(self, nums: List[int]) -> int:
        factors = dict()
        result = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            primes = self.getPrimes(num)
            for prime in primes:
                if prime not in factors:
                    factors[prime] = []
                factors[prime].append(i)
        uf = UnionFind(n)

        for factor in factors.keys():
            if factor == 1: continue
            for i in range(len(factors[factor]) - 1):
                uf.union(factors[factor][i], factors[factor][i + 1])
                
        groupSize = [0 for i in range(n)]
        
        for i in range(n):
            group = uf.find(i)
            groupSize[group] += 1
            result = max(result, groupSize[group])
        return result