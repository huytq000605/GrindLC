class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 0
        j = 0
        maxdq = deque()
        mindq = deque()
        for i in range(len(nums)):
            while maxdq and nums[i] > maxdq[-1]: maxdq.pop()
            while mindq and nums[i] < mindq[-1]: mindq.pop()
            maxdq.append(nums[i])
            mindq.append(nums[i])
            while maxdq[0] - mindq[0] > limit:
                if nums[j] == maxdq[0]: maxdq.popleft()
                if nums[j] == mindq[0]: mindq.popleft()
                j += 1
            result = max(result, i - j + 1)
        return result
