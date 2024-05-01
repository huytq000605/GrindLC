class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = sorted([nums1[i] - nums2[i] for i in range(n)])
        j = n-1
        result = 0
        for i in range(n):
            while j > i and diff[i] + diff[j] > 0:
                j -= 1
            result += n - max(i, j) - 1
        return result
        
