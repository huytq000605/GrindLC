class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)
        k = target // s
        target = target % s
        if target == 0:
            return len(nums) * k
        
        nums += nums
        d = dict()
        d[0] = -1
        result = math.inf
        cur = 0
        for i, num in enumerate(nums):
            if cur - target in d:
                result = min(result, i - d[cur - target])
            d[cur] = i
            cur += num
        if result == math.inf:
            return -1
        return result + k * n
