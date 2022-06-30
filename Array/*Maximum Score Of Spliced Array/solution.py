class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(a1, a2):
            cur = 0
            result = 0
            for i in range(len(a1)):
                cur = max(cur + a2[i] - a1[i], a2[i] - a1[i])
                result = max(result, cur)
            return result
        
        return max(sum(nums1) + kadane(nums1, nums2),
                   sum(nums2) + kadane(nums2, nums1))
