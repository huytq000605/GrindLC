class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        result = 0
        graph = [[] for i in range(len(values))]
        for [e1, e2, time] in edges:
            graph[e1].append([e2, time])
            graph[e2].append([e1, time])
        bfs = deque([[0, 0, set()]])
        while len(bfs) > 0:
            [node, time, passed] = bfs.popleft()
            passed.add(node)
            if node == 0:
                result = max(result, sum([values[value] for value in passed]))
            for [nextNode, timeTake] in graph[node]:
                if time + timeTake > maxTime:
                    continue
                bfs.append([nextNode, time + timeTake, set.copy(passed)])
            
        return result