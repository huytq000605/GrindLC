class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # 1. considering we have 1 value a for i, j, k: (a | a) ^ a = a
        # 2. considering we have 2 values (a, b) for i, j, k:
            # (a | a) & b = a & b
            # (b | b) & a = b & a
            # (a | b) & a = aa | ab = a | ab = a
            # (b | a) & a = a
            # (a | b) & b = b
            # (b | a) & b = b
            # => = 0
        # 3. Considering we have 3 values (a,b,c) for i, j, k:
            # For each (a | b) & c, we would have (b | a) & c => = 0
        # 4. Conclusion: We only have case 1, so xor all numbers 
        xor = 0
        for num in nums:
            xor ^= num
        return xor
