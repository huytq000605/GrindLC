class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        def min_ops(a, b):
            ops = 0
            for i in range(n-1):
                if a[i] > a[-1] or b[i] > b[-1]:
                    ops += 1
                    if b[i] > a[-1] or a[i] > b[-1]:
                        return math.inf
            return ops
                    
        # keep last elements the same
        result = min_ops(nums1, nums2)
        # swap last elements
        l1, l2 = nums1[-1], nums2[-1]
        nums1[-1], nums2[-1] = l2, l1
        result = min(result, min_ops(nums1, nums2) + 1)
        if result == math.inf: return -1
        return result
