class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        bits = [0 for _ in range(32)]
        for num in nums:
            bits[int(math.log2(num))] += 1
        
        missing_bit = 31
        ops = 0
        
        # Go from smallest to biggest because we don't lose anything if combine bits
        # But to split into smaller bits, each split cost us 1 operation
        for bit in range(31):
            if (target >> bit) & 1:
                if bits[bit]:
                    # use this bit for subsequence
                    bits[bit] -= 1
                else:
                    # we only need to care about smallest bit
                    # for example if we're missing bit 2,4,5
                    # on the way we split down to 2, we'll get 4, 5 also
                    missing_bit = min(missing_bit, bit)
            
            # if we're missing bits, can we split or not
            if missing_bit < bit and bits[bit]:
                ops += bit - missing_bit
                bits[bit] -= 1
                missing_bit = 31
            
            # combine bits
            bits[bit+1] += bits[bit] // 2
        
        # if there are still missing bits
        if missing_bit < 31:
            return -1
        
        return ops
