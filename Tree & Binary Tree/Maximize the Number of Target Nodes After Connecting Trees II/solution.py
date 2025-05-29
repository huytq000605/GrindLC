class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        def build_tree(edges, n):
            tree = [[] for _ in range(n)]
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree
        tree1 = build_tree(edges1, n)
        tree2 = build_tree(edges2, m)

        def dfs(tree, u, p):
            ro, re = 0, 1
            for v in tree[u]:
                if v == p: continue
                o, e = dfs(tree, v, u)
                ro += e
                re += o
            return ro, re
    
        o1, e1 = dfs(tree1, 0, -1)
        o2, e2 = dfs(tree2, 0, -1)
        add = max(o2, e2)

        dq = deque([(0, -1)])
        result = [0 for _ in range(n)]
        take_even = 1
        while dq:
            for _ in range(len(dq)):
                u, p = dq.popleft()
                for v in tree1[u]:
                    if v == p: continue
                    dq.append((v, u))
                result[u] = (e1 if take_even else o1) + add
            take_even ^= 1

        return result
