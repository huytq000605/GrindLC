class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda meeting: meeting[2])
        result = set()
        result.add(0)
        result.add(firstPerson)
            
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            graph = collections.defaultdict(list)
            knowSecret = set()
            stack = []
            while i < len(meetings) and meetings[i][2] == time:
                p1, p2, t = meetings[i]
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in result and p1 not in knowSecret:
                    knowSecret.add(p1)
                    stack.append(p1)
                if p2 in result and p2 not in knowSecret:
                    knowSecret.add(p2)
                    stack.append(p2)
                i += 1
			# Use DFS or BFS here
            while stack:
                person = stack.pop()
                for nextPerson in graph[person]:
                    if nextPerson not in knowSecret:
                        knowSecret.add(nextPerson)
                        stack.append(nextPerson)
                        
            result.update(knowSecret)
            
        return result