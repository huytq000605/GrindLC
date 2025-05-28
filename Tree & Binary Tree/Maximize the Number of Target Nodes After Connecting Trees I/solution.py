class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
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

        def bfs(tree, u, k):
            if k < 0: return 0
            dq = deque([(u, -1)])
            result = 1
            while dq and k:
                for _ in range(len(dq)):
                    u, p = dq.popleft()
                    for v in tree[u]:
                        if v == p: continue
                        dq.append((v, u))
                        result += 1
                k -= 1
            return result
        
        add = max([bfs(tree2, u, k-1) for u in range(m)])
        return [bfs(tree1, u, k) + add for u in range(n)]
