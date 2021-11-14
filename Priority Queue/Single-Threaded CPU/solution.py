import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        idx = 0
        result = []
        time = tasks[0][0]
        while idx < len(tasks) or len(heap):
            while idx < len(tasks) and tasks[idx][0] <= time:
                heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if len(heap) == 0 and idx < len(tasks):
                time = tasks[idx][0]
                continue
            [endTime, taskIndex] = heappop(heap)
            time = time + endTime
            result.append(taskIndex)
        return result