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
        def get(idx):
            return mountain_arr.get(idx)
        
        
        left, right = 1, n - 2
        mid = left + (right - left) // 2
        while not (get(mid) > get(mid - 1) and get(mid) > get(mid + 1)):
            if get(mid - 1) > get(mid + 1):
                right = mid - 1
                mid = left + (right - left) // 2
            else:
                left = mid + 1
                mid = left + (right - left) // 2
        peak = mid
        
        start = 0
        end = peak
        while start < end:
            mid = start + (end - start) // 2
            value = get(mid)
            if value < target:
                start = mid + 1
            else:
                end = mid
                
        if get(start) == target:
            return start
        
        start = peak + 1
        end = n - 1
        while start < end:
            mid = start + (end - start) // 2
            value = get(mid)
            if value > target:
                start = mid + 1
            else:
                end = mid
                
        if get(start) == target:
            return start
        
        return -1