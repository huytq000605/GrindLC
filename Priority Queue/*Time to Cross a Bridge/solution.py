class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # [leftToRighti, pickOldi, rightToLefti, putNewi].

        # (is_left, efficiency, idx)
        free = []
        # (free_time, idx, is_left)
        busy = []
        t = 0
        result = 0
        def eff(i):
            return (-time[i][0]-time[i][2], -i)
        
        for i, (ltr, po, rtl, pn) in enumerate(time):
            heappush(free, (1, eff(i), i))
            
        while n > 0 or busy or free:
            # free all busy workers
            while busy and t >= busy[0][0]:
                _, idx, is_left = heappop(busy)
                heappush(free, (is_left, eff(idx), idx))
            
            while n == 0 and free and free[0][0] == 1:
                heappop(free)
            
            if not free:
                if busy:
                    t = busy[0][0]
                continue

            # get the most priority one
            left, _, idx = heappop(free)
            if left:
                t += time[idx][0] # cross left to right
                heappush(busy, (t + time[idx][1], idx, 0))
                n -= 1 # Picking up one
            else:
                t += time[idx][2]
                result = max(result, t)
                heappush(busy, (t + time[idx][3], idx, 1))
                
        return result
        
