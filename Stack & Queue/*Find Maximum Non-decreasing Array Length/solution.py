class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0 for _ in range(n + 1)]
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        # dp[i] means the longest length of number of subarray for first i elements
        dp = [0 for _ in range(n + 1)]
        # last[i] means the optimal value of last subarray, building for first i elements
        last = [0 for _ in range(n + 1)]

        # dp[i] always >= dp[i-1], because nums[i] can be merge into last subarray
        # dp[i] = dp[j] + 1 if last[j] <= prefix[i] - prefix[j]
        # => prefix[j] + last[j] <= prefix[i]
        # Maintain a monotonic stack of prefix[j] + last[j]
        stack = [0]
        stack_ptr = 0
        for i in range(1, n+1):
            stack_ptr = min(stack_ptr, len(stack) - 1)
            # dp[i] >= d[j] for i >= j so we always want to try to move up if can
            while stack_ptr + 1 < len(stack) and \
                last[stack[stack_ptr + 1]] + prefix[stack[stack_ptr + 1]] <= prefix[i]:
                stack_ptr += 1

            j = stack[stack_ptr]
            dp[i] = dp[j] + 1
            last[i] = prefix[i] - prefix[j]

            while stack and last[stack[-1]] + prefix[stack[-1]] >= last[i] + prefix[i]:
                stack.pop()
            stack.append(i)
        return dp[-1]

            



            
