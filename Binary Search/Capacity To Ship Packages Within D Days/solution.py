class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = 1
        end = sum(weights)
        
        def valid(cap):
            trips = 1
            cur = 0
            for w in weights:
                if w > cap: return False
                if cur + w <= cap:
                    cur += w
                else:
                    cur = w
                    trips += 1
            return trips <= days
                    
            
        while start < end:
            mid = start + (end - start) // 2
            if valid(mid):
                end = mid
            else:
                start = mid + 1
        return start
