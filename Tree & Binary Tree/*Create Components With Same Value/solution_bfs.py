class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = [[] for i in range(n)]
        deg = [0 for i in range(n)]
        s = sum(nums)
        if len(edges) == 0:
            return 0
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            deg[u] += 1
            deg[v] += 1
        
        def bfs(val, deg, nums):
            q = deque([u for u, d in enumerate(deg) if d == 1])
            while q:
                u = q.popleft()
                if deg[u] == 0:
                    continue
                deg[u] = 0
                if nums[u] > val:
                    return False
                if nums[u] == val:
                    nums[u] = 0
                acted = False
                for v in tree[u]:
                    if deg[v] == 0: continue
                    acted = True
                    nums[v] += nums[u]
                    q.append(v)
                if nums[u] != 0 and not acted:
                    return False
            return True
            
                
        for val in range(1, s):
            if s % val == 0 and bfs(val, [*deg], [*nums]):
                return s // val - 1
        return 0
