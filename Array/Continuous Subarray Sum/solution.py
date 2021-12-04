class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        prefix = dict()
        prefix[0] = -1
        for i, num in enumerate(nums):
            total += num
            total %= k
            if total in prefix:
                if i - prefix[total] > 1:
                    return True
            else:
                prefix[total] = i
        return False