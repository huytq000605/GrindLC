class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        final_target = (1<<30) - 1
        for bit in range(29, -1, -1):
            # Try to remove bit from final target 
            target = final_target & ~(1 << bit)
            # Number of elements after operations
            valid = 0
            cur = (1 << 30) - 1
            for num in nums:
                cur &= num
                if cur | target == target:
                    valid += 1
                    cur = (1 << 30) - 1
            # if number of operations <= k
            if n - valid <= k:
                final_target = target
        return final_target
                
