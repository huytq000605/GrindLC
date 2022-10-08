class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = None
        for i in range(2, n):
            j, k = 0, i-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if result == None or abs(result - target) > abs(s - target):
                    result= s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return result
