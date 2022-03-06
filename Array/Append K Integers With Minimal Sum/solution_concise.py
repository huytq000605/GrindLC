class Solution:
	def minimalKSum(self, nums: List[int], k: int) -> int:
		result = k * (k + 1) // 2
		last = k + 1
		for num in sorted(set(nums)):
			if num < last:
				result += (last - num)
				last += 1
		return result