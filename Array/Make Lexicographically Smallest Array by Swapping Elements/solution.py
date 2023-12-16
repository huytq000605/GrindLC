class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [1 for _ in range(n)]
        self.idxs = [[i] for i in range(n)]
        self.n = n
    
    def find(self, u):
        if self.p[u] != u:
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
        self.idxs[u].extend(self.idxs[v])
        self.idxs[v] = []

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        uf = UF(n)
        for i in range(1, n):
            if nums[i][0] - nums[i-1][0] <= limit:
                uf.union(nums[i][1], nums[i-1][1])
        for num, idx in nums:
            if idx == uf.find(idx):
                uf.idxs[idx] = sorted(uf.idxs[idx], reverse = True)
        result = [*nums]
        for num, idx in nums:
            p = uf.find(idx)
            result[uf.idxs[p].pop()] = num
        return result
        
        
