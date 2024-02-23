from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
        # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
        # arr[i] - arr[j] <= diff
        n = len(nums1)
        nums = [nums1[i] - nums2[i] for i in range(n)]
        sl = SortedList()
        result = 0
        for num in nums:
            idx = sl.bisect_left(num + diff + 1)
            result += idx
            sl.add(num)
        return result
        
