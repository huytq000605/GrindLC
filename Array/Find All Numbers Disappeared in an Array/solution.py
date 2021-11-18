class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = set()
        # nums[i] = i + 1
        for i in range(n):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
				# Change nums[nums[i] - 1] cause if nums[i] changes make nums[nums[i] - 1] change
                nums[nums[i] - 1], nums[i]  = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                result.add(i+1)
        return list(result)