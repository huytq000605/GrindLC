class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        result = 0
        for i in range(n):
            t = 0
            # We can only delete nums[i] if there is at least 1 bigger num on the left (we call it nums[ft])
            # To delete nums[i], we also need to delete nums[j] for j with ft < j < i
            # Then the number of turns we need to delete nums[i] is max(no_of_turns[j] for ft < j < i) + lus (we will explain what is 1 here)
            while stack and nums[i] >= stack[-1][0]:
                last_num, times = stack.pop()
                t = max(t, times)
            # If there's no number in the stack that means nums[i] is a valid number in the final state
            # So we dont need to delete anything
            # If there's at least 1 number in the stack that means nums[i] need to be deleted, we + 1 turn to delete this number
            if stack:
                t += 1
            else:
                t = 0
            result = max(result, t)
            stack.append((nums[i], t))
            
        return result