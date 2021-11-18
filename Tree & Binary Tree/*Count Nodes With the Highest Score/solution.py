class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graph = [[] for i in range(n)]
        for i in range(1, n):
            graph[parents[i]].append(i)
        subTree = [[1, 1, 1] for i in range(n)]
            
        def dfs(node):
            if node == None:
                return 0
            totalLeftRight = 0
            for i, nextNode in enumerate(graph[node]):
                numOfNodes = dfs(nextNode)
                totalLeftRight += numOfNodes
                subTree[node][i] = max(1, numOfNodes)
            subTree[node][2] = max(1, n - totalLeftRight - 1)
            return totalLeftRight + 1
        
        dfs(0)
        
        result = 0
        highestScore = 0
        scores = [subTree[i][0] * subTree[i][1] * subTree[i][2] for i in range(n)]
        for score in scores:
            if highestScore < score:
                result = 1
                highestScore = score
            elif highestScore == score:
                result += 1
        return result