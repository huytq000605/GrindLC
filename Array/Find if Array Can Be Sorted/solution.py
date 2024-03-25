class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i, n = 0, len(nums)
        mx = -math.inf
        while i < n:
            # Process by group of adjacent elements have same set bits.
            if nums[i] < mx: return False
            nmx = max(mx, nums[i])
            i += 1
            while i < n and nums[i].bit_count() == nums[i-1].bit_count():
                if nums[i] < mx: return False
                nmx = max(nmx, nums[i])
                i += 1
            mx = nmx
        return True
