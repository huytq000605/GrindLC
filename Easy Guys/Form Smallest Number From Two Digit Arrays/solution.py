class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        result = math.inf
        for num in nums1:
            if num in nums2:
                result = min(result, num)
        return min(result, nums1[0] * 10 + nums2[0], nums2[0] * 10 + nums1[0])
