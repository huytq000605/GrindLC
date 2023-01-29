class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        if k == 0:
            for i in range(n): 
                if nums1[i] != nums2[i]: return -1
            return 0
        
        ops = 0
        balance = 0
        for i in range(n):
            diff = nums2[i] - nums1[i]
            if diff % k != 0: return -1
            if diff > 0:
                ops += diff // k
            balance += diff
        if balance != 0:
            return -1
        return ops
