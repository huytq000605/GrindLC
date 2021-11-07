class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        result = 0
        graph = {}
        for [e1, e2, time] in edges:
            if e1 not in graph:
                graph[e1] = []
            if e2 not in graph: 
                graph[e2] = []
            graph[e1].append([e2, time])
            graph[e2].append([e1, time])
        passed = set()
        passed.add(0)
            
        def dfs(node, time):
            nonlocal result
            nonlocal passed
            if node == 0:
                result = max(result, sum([values[value] for value in passed]))
            if node in graph:
                for [nextNode, timeTake] in graph[node]:
                    if nextNode != 0 and time + timeTake * 2 > maxTime:
                        continue
                    if time + timeTake > maxTime:
                        continue
                    alreadyPassed = False
                    if nextNode in passed:
                        alreadyPassed = True
                    passed.add(nextNode)
                    dfs(nextNode, time + timeTake)
                    if not alreadyPassed:
                        passed.remove(nextNode)
                        
        dfs(0, 0)
        return result