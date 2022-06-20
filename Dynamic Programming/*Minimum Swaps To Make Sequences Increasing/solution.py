class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # changed[i] is min num of swap to have sorted nums1[:i+1], nums2[:i+1] && we must swap at i
        changed = [n for i in range(n)]
        
        # not_changed[i] is min num of swap to have sorted nums1[:i+1], nums2[:i+1] && we must not swap at i
        not_changed = [n for j in range(n)]
        
        changed[0] = 1
        not_changed[0] = 0
        
        for i in range(1, n):
            # We only have 2 cases, the inputs guarantee that
            # Since we only need the last value from dp array => We can optimize this to O(1) space
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                not_changed[i] = not_changed[i-1]
                changed[i] = changed[i-1] + 1
            
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                not_changed[i] = min(not_changed[i], changed[i-1])
                changed[i] = min(changed[i], not_changed[i-1] + 1)
        return min(changed[-1], not_changed[-1])