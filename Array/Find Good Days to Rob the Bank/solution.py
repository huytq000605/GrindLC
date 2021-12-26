class Solution:
    def goodDaysToRobBank(self, nums: List[int], time: int) -> List[int]:
        n = len(nums)
        if time == 0:
            return [i for i in range(n)]
        prefix = [0 for i in range(n)]
        suffix = [0 for i in range(n)]
        result = []
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                prefix[i] = prefix[i-1] + 1
        
        for i in range(n - 2, -1 ,-1):
            if nums[i] <= nums[i+1]:
                suffix[i] = suffix[i+1] + 1

        for i in range(n):
            if prefix[i] >= time and suffix[i] >= time:
                result.append(i)
        return result