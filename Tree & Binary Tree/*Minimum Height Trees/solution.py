class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leafs = []
        seen = set()
        
        for i in range(n):
            if len(graph[i]) <= 1:
                seen.add(i)
                leafs.append(i)
        
        while n - len(seen) + len(leafs) > 2:
            nextLeafs = []
            while leafs:
                leaf = leafs.pop()
                for adj in graph[leaf]:
                    graph[adj].remove(leaf)
                    if len(graph[adj]) == 1:
                        seen.add(adj)
                        nextLeafs.append(adj)
            leafs = nextLeafs
        
        return leafs