class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        idx = 0
        changed = False
        while idx < len(nums) or changed:
            changed = False
            if len(stack) >= 2:
                last = stack[-1]
                prev_last = stack[-2]
                lcm = math.lcm(last, prev_last)
                gcd = last * prev_last // lcm
                if gcd > 1:
                    changed = True
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                    continue
            if idx < len(nums):
                stack.append(nums[idx])
                changed = True
                idx += 1
        return stack