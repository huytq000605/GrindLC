class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        
        result = [0 for i in range(n)]
        sumNodesDownward = [0 for i in range(n)]
        numNodesDownward = [0 for i in range(n)]
    
        def dfs(node, parent):
            # return numOfNodes, sumDistance
            numOfNodes = 1
            sumDistance = 0
            for child in graph[node]:
                if child == parent:
                    continue
                numNodes, sumNodes = dfs(child, node)
                numOfNodes += numNodes
                sumDistance += sumNodes + numNodes
            
            sumNodesDownward[node] = sumDistance
            numNodesDownward[node] = numOfNodes
            return numOfNodes, sumDistance
        dfs(0, -1)
        
        result[0] = sumNodesDownward[0]
        def dfs2(node, parent):
            if parent != -1:
                result[node] = sumNodesDownward[node] + (result[parent] - sumNodesDownward[node] - numNodesDownward[node]) + (n - numNodesDownward[node])
            for child in graph[node]:
                if child == parent:
                    continue
                dfs2(child, node)
        dfs2(0, -1)
        return result
            