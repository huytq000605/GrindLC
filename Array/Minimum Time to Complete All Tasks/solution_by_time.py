class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort()
        ongoing = []
        idx = 0
        result = 0
        for time in range(2001):
            while True and idx < len(tasks):
                s,e,d = tasks[idx]
                if s > time:
                    break
                ongoing.append([e, d])
                idx += 1
                
            need_work = False
            for end, duration in ongoing:
                if end - time + 1 == duration:
                    need_work = True
                    break
            
            if need_work:
                result += 1
                n = len(ongoing)
                for i in range(n):
                    ongoing[i][1] -= 1
                
                new_ongoing = []
                for task in ongoing:
                    if task[1] > 0:
                        new_ongoing.append(task)
                ongoing = new_ongoing
                
                
        return result
