class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1) + 1
        tree1 = [[] for _ in range(n)]
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
            
        tree2 = [[] for _ in range(n)]
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        
        max_single_diameter = 0
        
        min_branch = math.inf
        def diameter1(u, p, depth = 0):
            nonlocal max_single_diameter, min_branch
            mx = 0
            for v in tree1[u]:
                if v == p: continue
                d = diameter1(v, u, depth + 1)
                max_single_diameter = max(max_single_diameter, d + 1 + mx)
                mx = max(mx, d)
            min_branch = min(min_branch, max(depth, mx + 1))
            return mx + 1
        
        combined_diameter = math.inf
        def diameter2(u, p, depth = 0):
            nonlocal max_single_diameter, combined_diameter
            mx = 0
            for v in tree2[u]:
                if v == p: continue
                d = diameter2(v, u, depth + 1)
                max_single_diameter = max(max_single_diameter, d + 1 + mx)
                mx = max(mx, d)
            combined_diameter = min(combined_diameter, min_branch + max(depth, mx + 1))
            return mx + 1
        
        diameter1(0, -1)
        diameter2(0, -1)
        print(max_single_diameter, min_branch, combined_diameter)
        # return max(combined_diameter, max_single_diameter)
        return 0
