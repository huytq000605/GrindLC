class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda task: task[1])
        result = 0
        done = [0 for _ in range(2001)]
        for task in tasks:
            start, end, duration = task
            for i in range(start, end + 1):
                if done[i]:
                    duration -= 1
            i = end
            while duration > 0:
                if not done[i]:
                    done[i] = 1
                    duration -= 1
                i -= 1 
                
        return sum(done)
