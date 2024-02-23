class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]

    def find(self, u):
        if u != self.p[u]:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.r[u] < self.r[v]:
            u, v = v, u
        self.r[u] += self.r[v]
        self.p[v] = u

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        uf = UF(n)
        factors = {}

        def get_factors(num):
            factors = set()
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    factors.add(num // i)
            if num != 1:
                factors.add(num)
            return factors

        for i, num in enumerate(nums):
            num_factors = get_factors(num)
            for factor in num_factors:
                if factor in factors:
                    uf.union(factors[factor], i)
                factors[factor] = i

        return max(uf.r) == n
