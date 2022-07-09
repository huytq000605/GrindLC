class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        result = [0 for i in range(n-k+1)]
        for i in range(n):
            while dq and (i - dq[0][1] + 1) > k:
                dq.popleft()
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append((nums[i], i))
            if i >= k-1:
                result[i-k+1] = dq[0][0]
        return result
