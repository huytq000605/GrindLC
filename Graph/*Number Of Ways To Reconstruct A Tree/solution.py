class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)

        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)
            
        def dfs(node, seen, trees):
            for adj in graph[node]:
                if adj in seen:
                    continue
                trees[-1].append(adj)
                seen.add(adj)
                dfs(adj, seen, trees)
        
        def check_tree(nodes):
            root = -1
            many_roots = False
            for node in nodes:
                if len(graph[node]) == len(nodes) - 1:
                    if root != -1:
                        many_roots = True
                        break
                    else:
                        root = node

            if root == -1:
                return 0
            
            for adj in graph[root]:
                graph[adj].remove(root)
                        
            trees = []
            seen = set()
           for node in nodes:
                if node == root or node in seen:
                    continue
                trees.append([node])
                seen.add(node)
                dfs(node, seen, trees)
            
            many_ways = many_roots
            for tree in trees:
                check_value = check_tree(tree)
                if check_value == 0:
                    return 0
                elif check_value == 2:
                    many_ways = True
            
            if many_ways:
                return 2
            return 1
            
        return check_tree(graph.keys()) 
