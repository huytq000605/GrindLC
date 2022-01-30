class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
      n = len(nums)
      result = []
      i, j = 0, 0
      while i < n and j < n:
        while nums[i] < 0: i += 1
        while nums[j] > 0: j += 1
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1
      return result