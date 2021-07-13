from typing import List
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if freq.get(task) == None: freq[task] = 0
            freq[task] += 1
        
        freqHeap = []
        for (remaining) in freq.items():
            heappush(freqHeap, (-remaining))
            
        cooldownHeap = []
        currentTime = 0
        
        while len(freqHeap) > 0 or len(cooldownHeap) > 0:
            while len(cooldownHeap) > 0:
                time, remaining = heappop(cooldownHeap)
                if currentTime - time <= n:
                    heappush(cooldownHeap, (time, remaining))
                    break
                else:
                    heappush(freqHeap, (remaining))
            
            if len(freqHeap) > 0:
                remaining = heappop(freqHeap)
                if (-remaining) > 1:
                    heappush(cooldownHeap, (currentTime, remaining + 1))
            
            currentTime += 1
        
        return currentTime
            
