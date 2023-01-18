class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mn, mx = nums[0], nums[0]
        cmn, cmx, s = 0, 0, 0
        for num in nums:
            cmn = min(cmn + num, num)
            cmx = max(cmx + num, num)
            mn = min(mn, cmn)
            mx = max(mx, cmx)
            s += num
        if mx < 0:
            return mx
        return max(mx, s - mn)
