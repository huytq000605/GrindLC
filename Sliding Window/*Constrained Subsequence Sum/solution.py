class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dq = deque()
        for i, num in enumerate(nums):
            while dq and i - dq[0][1] > k:
                dq.popleft()
            prev = 0
            if dq:
                prev = max(0, dq[0][0])
            dp[i] = prev + num
            while dq and dq[-1][0] <= dp[i]:
                dq.pop()
            dq.append((dp[i], i))
        return max(dp)
