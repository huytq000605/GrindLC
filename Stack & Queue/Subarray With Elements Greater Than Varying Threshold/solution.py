class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        next_lower = [n for i in range(n)]
        prev_lower = [-1 for i in range(n)]

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_lower[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] > nums[i]:
                prev_lower[stack.pop()] = i
            stack.append(i)

        for i in range(n):
            prev = prev_lower[i]
            nxt = next_lower[i]
            length = (nxt-1) - (prev+1) + 1
            if nums[i] > threshold / length:
                return length
        return -1
