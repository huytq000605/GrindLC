class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        d1, d2 = divisor1, divisor2
        u1, u2 = uniqueCnt1, uniqueCnt2
        
        lcm = math.lcm(d1, d2)
        start, end = u1 + u2, 10**10
        while start < end:
            mid = start + (end - start) // 2
            v1 = (mid - mid // d1) >= u1
            v2 = (mid - mid // d2) >= u2
            v3 = (mid - mid // lcm) >= (u1 + u2)
            
            if v1 and v2 and v3:
                end = mid
            else:
                start = mid + 1
        return start
