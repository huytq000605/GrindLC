class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t < abs(fx - sx):
            return False
        if t < abs(fy - sy):
            return False
        if sx == fx and sy == fy and t == 1:
            return False
        return True
