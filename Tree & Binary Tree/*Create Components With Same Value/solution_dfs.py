class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = [[] for i in range(n)]
        s = sum(nums)
        
        def dfs(u, prev, val):
            cur = nums[u]
            for v in tree[u]:
                if v == prev:
                    continue
                cur += dfs(v, u, val)
            if cur == val:
                return 0
            return cur
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        for val in range(1, s):
            if s % val == 0 and dfs(0, -1, val) == 0:
                return s // val - 1
        return 0
