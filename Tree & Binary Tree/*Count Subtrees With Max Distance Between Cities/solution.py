class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        result = [0] * (n-1)
        
        def maxDistance(subTree):
            cities = 0
            randomStart = -1
            for i in range(n): # count cities in subtree and choose a random starting city
                if (subTree >> i) & 1 == 1:
                    if cities == 0:
                        randomStart = i
                    cities += 1
                    
            visited = set()
            furthest = [-1, -1] # furthest node, distance to furthest node
            def dfs(node, parent, length):
                nonlocal furthest
                visited.add(node)
                if length > furthest[1]:
                    furthest = [node, length]
                for nextNode in graph[node]:
                    if (subTree >> nextNode) & 1 == 0 or nextNode == parent:
                        continue
                    dfs(nextNode, node, length + 1)
            dfs(randomStart, -1, 0)
            
            if len(visited) != cities: # Because we dfs all tree, diff => invalid tree
                return 0
            
            furthestNode = furthest[0]
            furthest = [-1, -1]
            dfs(furthestNode, -1, 0)
            return furthest[1]
        
        for edge1, edge2 in edges:
            graph[edge1 - 1].append(edge2 - 1)
            graph[edge2 - 1].append(edge1 - 1)
        
        for subtree in range(1 << n):
            max_distance = maxDistance(subtree)
            if max_distance > 0:
                result[max_distance - 1] += 1 # 1-indexed
                
                
        return result
        