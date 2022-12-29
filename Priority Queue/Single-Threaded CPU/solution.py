class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((enq, proc, idx) for idx, (enq, proc) in enumerate(tasks))
        queue_tasks = []
        idx = 0
        time = 0
        result = []
        while idx < len(tasks) or queue_tasks:
            if len(queue_tasks) == 0:
                time = max(time, tasks[idx][0])
            while idx < len(tasks) and time >= tasks[idx][0]:
                heappush(queue_tasks, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            process_time, task = heappop(queue_tasks)
            result.append(task)
            time = time + process_time
        return result
