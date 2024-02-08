class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        tree = [[] for _ in range(n)]
        for u, p in enumerate(parents):
            if p == -1: continue
            tree[p].append(u)
        
        result = [1 for _ in range(n)]
        consider_root = -1
        for u, num in enumerate(nums):
            if num == 1:
                consider_root = u
                break
        if consider_root == -1:
            return result
        seen = set()

        def dfs(u):
            nonlocal seen
            if nums[u] in seen: return
            seen.add(nums[u])
            for v in tree[u]:
                dfs(v)
        
        value = 1
        while consider_root != -1:
            dfs(consider_root)
            while value in seen:
                value += 1
            result[consider_root] = value
            consider_root = parents[consider_root]
        return result

