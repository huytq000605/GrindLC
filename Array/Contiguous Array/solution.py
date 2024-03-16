class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = dict()
        prefix[0] = -1
        result = 0
        cur = 0
        for i, num in enumerate(nums):
            cur += num if num == 1 else -1
            if cur in prefix:
                result = max(result, i - prefix[cur])
            else:
                prefix[cur] = i
        return result
