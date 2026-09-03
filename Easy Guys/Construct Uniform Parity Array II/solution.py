class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        all_odd = True
        all_even = True
        mn = min(nums1)
        for num in nums1:
            all_odd = all_odd and ((num & 1) == 1)
            all_even = all_even and ((num & 1) == 0)
        if all_odd or all_even: return True
        return (mn & 1) == 1
