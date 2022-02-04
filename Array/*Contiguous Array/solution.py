class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = dict()
        seen[0] = -1
        cur = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                cur -= 1
            if cur in seen:
                result = max(result, i - seen[cur])
            else:
                seen[cur] = i
        return result
