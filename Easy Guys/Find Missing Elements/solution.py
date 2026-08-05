class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        d = [0 for _ in range(mx+1)]
        for num in nums: d[num] = 1
        return [num for num in range(mn, mx+1) if not d[num]]
