import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[profits[i], capital[i]] for i in range(len(profits))]
        projects.sort(key= lambda project: project[1])
        idx = 0
        heap = []
        while k > 0:
            while idx < len(projects) and projects[idx][1] <= w:
                heappush(heap, -projects[idx][0])
                idx += 1
            if len(heap) == 0: break
            w += -heappop(heap)
            k -= 1
        return w