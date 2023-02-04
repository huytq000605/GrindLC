class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def cal_gcd(a, b):
            if a < b:
                a, b = b,a
            if b == 0:
                return a
            return cal_gcd(b, a % b)
        # gcd(1,1) = 1
        # mutiply by 2 can make gcd doubled
        # do (x, y) into (x-y, y) or (x, y-x) will let gcd be the same
        gcd = cal_gcd(targetX, targetY)
        while gcd > 1:
            if gcd & 1 == 1: return False
            gcd >>= 1
        return True
