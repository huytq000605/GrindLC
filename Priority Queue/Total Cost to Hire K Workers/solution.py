class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        first = costs[:candidates]
        last = costs[max(candidates, n - candidates):]
        heapify(first)
        heapify(last)
        i, j = candidates, n-1-candidates
        result = 0
        while k > 0:
            k -= 1
            if not last or (first and first[0] <= last[0]):
                result += heappop(first)
                if i <= j:
                    heappush(first, costs[i])
                    i += 1
            else:
                result += heappop(last)
                if i <= j:
                    heappush(last, costs[j])
                    j -= 1
        return result
                    
                    
        
