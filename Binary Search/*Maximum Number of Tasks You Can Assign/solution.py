from typing import *
from math import *
# len(tasks) = n
# len(workers) = m
# Time complexity: nlogn + mlogm + log(min(m,n))^2 * min(m,n)^2
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        # O
        tasks.sort()
        workers.sort(reverse = True)
        def isValid(k):
            lowTasks = tasks[:k]
            highWorkers = workers[:k][::-1]
            p = pills
            s = strength
            i = 0
            for worker in highWorkers:       
                task = lowTasks[i]
                if worker >= task:
                    i += 1
                    continue
                else:
                    if p > 0:
                        worker += s
                        p -= 1
                        start = i
                        end = len(lowTasks) - 1
                        while start < end:
                            mid = start + ceil((end - start + 1) / 2)
                            if worker >= lowTasks[mid]:
                                start = mid
                            else:
                                end = mid - 1
                        if worker < lowTasks[start]:
                            return False
                        if i == start:
                            i += 1
                        else:
                            lowTasks.pop(start)
                    else:
                        return False
            return True
                        
                        
            
        start = 0
        end = min(len(workers), len(tasks))
        while start < end:
            mid = start + ceil((end - start + 1) / 2)
            if(isValid(mid)):
                start = mid
            else:
                end = mid - 1
                
        return start