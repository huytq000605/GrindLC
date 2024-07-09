class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, z2 = 0, 0
        s1, s2 = 0, 0
        for num in nums1:
            s1 += num + (num == 0)
            z1 += num == 0
        for num in nums2:
            s2 += num + (num == 0)
            z2 += num == 0
        if s1 < s2 and not z1:
            return -1
        if s2 < s1 and not z2:
            return -1

        return max(s1, s2)
