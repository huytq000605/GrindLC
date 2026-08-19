class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = -1
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if k == n or (counter[num] == 1 and (i == 0 or i == n-1 or k == 1)):
                result = max(result, num)
        return result
