class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack = []
        stack2 = []
        n = len(nums)
        next_greater = [-1 for i in range(n)]
        for i, num in enumerate(nums):
            while stack2 and num > nums[stack2[-1]]:
                next_greater[stack2.pop()] = num
            tmp = []
            while stack and num > nums[stack[-1]]:
                tmp.append(stack.pop())
            if tmp:
                stack2 += tmp[::-1]
            stack.append(i)
        return next_greater
