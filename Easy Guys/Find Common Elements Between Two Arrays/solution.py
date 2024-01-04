class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        s1, s2 = set(nums1), set(nums2)
        r = [0, 0]
        for num in nums1:
            if num in s2: r[0] += 1
        for num in nums2:
            if num in s1: r[1] += 1
        return r
