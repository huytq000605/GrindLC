class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        mx = max(nums)
        diffs = [mx - num for num in nums]
        mx = max(diffs)
        total = sum(diffs)
        # There are 4 cases
        
        # 1. if cost1 * 2 <= cost2 or len(nums) < 3, just use all cost1
        if cost1 * 2 <= cost2 or len(nums) < 3: 
            return (total * cost1) % MOD
        
        # 2. try to use cost2 as much as we can up to max(nums), the rest use cost1
        # LC1953: https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/description/
        # If(max <= sum except max) can always make pair
        # Else can only do (max - sum except max) * 2 as pair
        # Left with max - sum except max
        # = max - (total - max)
        # = 2 * max - total
        c1 = max(0, mx * 2 - total)
        c2 = total - c1
        result = (c1 + c2 % 2) * cost1 + c2//2 * cost2

        # 3. try to use cost2 as much as we can, even exceeding max(nums), but in the end still use cost1 to fill, this is only lowering cost1
        # Use cost2 between mx element and n-1 elements
        # look at c1 = max(0, mx*2 - total)
        # => c1 = (mx+1) * 2 - (total + n) =  c1 - (n-2)
        # => reduce cost 1 by n-2
        total += c1 // (n-2) * n
        c1 %= n-2
        c2 = total - c1
        result = min(result, (c1 + c2 % 2) * cost1 + c2//2 * cost2)
        
        # 4. we don't want to use operation 1 from 3. as well
        # we keep using operation 2 until everything is equal
        # there can be 2 sub-cases in this
        # a. we increase by n, but still need to use op1 due to total being odd
        # b. we increase once more, now no longer odd
        for i in range(2):
            total += n
            result = min(result, (total % 2) * cost1 + total // 2 * cost2)
        return result % MOD

