class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = dict()
        seen[0] = -1
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            cur %= k
            if cur in seen:
                if i - seen[cur] > 1:
                    return True
            else:
                seen[cur] = i
        return False
