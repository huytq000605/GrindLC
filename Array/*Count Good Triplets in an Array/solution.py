from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        idxs = dict()
        n = len(nums1)
        for idx, num in enumerate(nums2):
            idxs[num] = idx
        
        result = 0
        for idx, num in enumerate(nums1):
            nums1[idx] = idxs[num]
        
        arr = SortedList()
        for num in nums1:
            arr.add(num)
            # Binary Search
            start = arr.index(num)
            left = start
            right = n - (num + 1) - (len(arr) - 1 - (start + 1) + 1)

            result += left * right
        return result