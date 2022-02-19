class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        squeries = []
        sintervals = []
        
        for i, query in enumerate(queries):
            squeries.append((query, i))
    
        for i, interval in enumerate(intervals):
            sintervals.append((*interval, i))
            
        squeries.sort()
        sintervals.sort()
        
        result = [-1 for i in range(len(queries))]
        
        interval_idx = 0
        heap = []
        
        for query, idx in squeries:
            while interval_idx < len(intervals) and sintervals[interval_idx][0] <= query:
                start, end, jdx = sintervals[interval_idx]
                heappush(heap, (end - start + 1, start, end, jdx))
                interval_idx += 1
                
            while len(heap) > 0 and heap[0][2] < query:
                heappop(heap)
            
            if len(heap) > 0:
                result[idx] = heap[0][0]
        
        return result