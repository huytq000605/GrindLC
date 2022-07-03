class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Could be optimize to O(1) space because only based on previous value
        # up[i] is the longest wiggle subsequence end at idx i and wiggle up at i
        # down[i] is the longest wiggle subsequence end at idx i and wiggle down at i
        n = len(nums)
        up = [1 for i in range(n)]
        down = [1 for i in range(n)]
        for i in range(1, n):
            up[i] = up[i-1]
            down[i] = down[i-1]
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
        return max(up[-1], down[-1])
