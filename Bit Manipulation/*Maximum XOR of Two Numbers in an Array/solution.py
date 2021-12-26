class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
				# current masks for all nums
        masks = [0 for i in range(n)]
        for i in range(31, -1, -1):
						# update masks for all nums
            for j in range(n):
                masks[j] |= nums[j] & (1 << i)
            
						# can be next result
            nextResult = result | (1 << i)

						# If have 2 mask xor with each other = nextResult then result = nextResult
            seen = set()
            for mask in masks:
                if mask ^ nextResult in seen:
                    result = nextResult
                    break
                seen.add(mask)
        return result
                