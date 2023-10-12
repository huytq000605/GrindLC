# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        @cache
        def get(n):
            return mountain_arr.get(n)
        
        start = 1
        end = n-2
        while start < end:
            i = start + (end - start) // 2
            a = get(i-1)
            b = get(i)
            if a > b:
                end = i-1
                continue
            c = get(i+1)
            if a < b and b > c:
                start = i
                break
            if c > b:
                start = i+1
                continue
        peak = start

        start = 0
        end = peak
        while start < end:
            mid = start + (end - start) // 2
            if get(mid) < target:
                start = mid + 1
            else:
                end = mid
        if get(start) == target:
            return start
        
        start = peak + 1
        end = n-1
        while start < end:
            mid = start + (end - start) // 2
            if get(mid) > target:
                start = mid + 1
            else:
                end = mid
        if get(start) == target:
            return start
        
        return -1
        
        
            
