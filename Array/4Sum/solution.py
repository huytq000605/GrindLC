class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, k, target):
            nums.sort()
            result = []
            def dfs(left, right, k, target, current):
                nonlocal result
                if k == 2:
                    while left < right:
                        if nums[left] + nums[right] == target:
                            result.append([*current, nums[left], nums[right]])
                            left += 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                        elif nums[left] + nums[right] < target:
                            left += 1
                        else:
                            right -= 1
                else:
                    while left < right:
                        dfs(left + 1, right, k - 1, target - nums[left], [*current, nums[left]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
            dfs(0, len(nums) - 1, k, target, [])
            return result
        return kSum(nums, 4, target)
