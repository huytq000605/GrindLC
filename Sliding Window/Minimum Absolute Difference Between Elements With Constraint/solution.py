from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sl = SortedList()
        n = len(nums)
        result = math.inf
        for i in range(x, n):
            sl.add(nums[i-x])
            j = sl.bisect_left(nums[i])
            for k in [j-1, j]:
                if k >= 0 and k < len(sl):
                    result = min(result, abs(nums[i] - sl[k]))
        return result
